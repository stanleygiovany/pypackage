import re
from pathlib import Path

from setuptools import setup, find_packages

FILE = Path(__file__).resolve()
REQUIREMENTS_CPU = [
    "pytest"
]
REQUIREMENTS_GPU = [
    "flask"
]
REQUIREMENTS = [
    "numpy"
]

setup(
    name="pypackage",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=REQUIREMENTS,
    extras_require={
        "cpu": REQUIREMENTS_CPU,
        "gpu": REQUIREMENTS_GPU
    }
)