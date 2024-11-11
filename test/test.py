# test/test_math_utils.py

import sys
import os
import pytest

from cyberonics_py import Robot, Device, DeviceProperty
from cyberonics_py.graphics import GraphicCell

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import cyberonics_py as cyber
import cyberonics_py.graphics as graphics

def test_robot():
    class Motor(Device):
        def __init__(self, name: str):
            self.speed = DeviceProperty(0., mutable=True)
            header = graphics.HeaderText(name)
            slider = graphics.Slider(managed_property=self.speed, min_value=0., max_value=1., step=0.1)
            self.speed.add_listener(lambda speed: self.set_speed(speed))
            self.device_cell = graphics.GraphicCell([header, slider])
            super().__init__(f"{self.__class__.__name__}--{name}", [self.speed], self.device_cell)

        def set_speed(self, speed: float):
            print("Setting motor speed to", speed)
            # TODO: Implement motor speed control logic here

    class Ava(Robot):
        def __init__(self):
            self.motor1 = Motor("Motor 1")
            self.motor2= Motor("Motor 2")
            super().__init__([self.motor1, self.motor2])

