import re
from pathlib import Path

from setuptools import setup, find_packages

FILE = Path(__file__).resolve()
REQUIREMENTS = [
    "numpy"
]

setup(
    name="pypackage",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=REQUIREMENTS
)