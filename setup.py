from distutils.core import setup
from setuptools import find_packages

setup(
    name = "snowflake",
    version = "0.1.1",
    author = "Primula Mukherjee",
    author_email = "primula.mukherjee@fau.de",
    license='Apache-2.0 license',
    packages = find_packages(),
    install_requires = ["numpy", "turtles"],
 )
