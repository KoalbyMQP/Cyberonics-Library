from setuptools import setup, find_packages

setup(
    name="cyberonics-py",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Skyler Wiernik",
    author_email="skwiernik@wpi.edu",
    description="Python library to interface with Cyberonics devices",
    long_description="Python library to interface with Cyberonics devices",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
