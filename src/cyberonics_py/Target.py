import threading
from abc import ABC, abstractmethod
from typing import Callable, TYPE_CHECKING, final
from multiprocessing import Process
import asyncio
import time
import os


if TYPE_CHECKING:
    from .Robot import Robot


class Target(ABC):

    

    def __init__(self, name: str, robot: 'Robot', shutdown_timeout: float = 0.5):
        self._name = name
        self.robot = robot
        self.shutdown_timeout = shutdown_timeout
        self.__worker: threading.Thread | None = None

        self.stdout_callback: Callable[[str], None] | None = None
        self.stderr_callback: Callable[[str], None] | None = None

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def _run(self) -> threading.Thread:
        raise NotImplementedError

    @final
    def run(self):
        self.__worker = self._run()


    @abstractmethod
    async def _shutdown(self, beat: Callable[[], None]):
        pass

    @final
    def _read_output(self, stream, callback):
        for line in iter(stream.readline, ''):
            if callback:
                callback(line.strip())
        stream.close()

    @final
    def shutdown(self) -> None:
        if self.__worker is None:
            return  # never started

        async def _shutdown_task():
            shutdown_done = asyncio.Event()
            last_beat = time.monotonic()

            def beat():
                nonlocal last_beat
                last_beat = time.monotonic()

            async def watchdog():
                # Poll every 100 ms for overdue heart‑beats
                while not shutdown_done.is_set():
                    await asyncio.sleep(0.1)
                    overdue = time.monotonic() - last_beat > self.shutdown_timeout
                    if overdue:
                        if self.__worker.is_alive():
                            # TODO: Create a better "hard shutdown"
                            print(
                                f"[WARNING] Worker thread '{self._name}' "
                                f"did not shut down within {self.shutdown_timeout}s. Detaching.")
                            # This just detaches the thread. It does not stop it from running.
                            self.__worker.daemon = True
                        shutdown_done.set()

            watchdog_task = asyncio.create_task(watchdog())
            try:
                await self._shutdown(beat)
            finally:
                shutdown_done.set()
                await watchdog_task

        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                loop.create_task(_shutdown_task())
            else:
                loop.run_until_complete(_shutdown_task())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(_shutdown_task())
