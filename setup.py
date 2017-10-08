"""Setup file."""

# external imports
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='search5bot',
   version='0.1',
   description='A telegram search bot',
   license="GPLv3",
   long_description=long_description,
   author='Jorge Chamorro, Luis Liñán',
   author_email='jorge@jorgechp.com, luislivilla@gmail.com',
   url="https://github.com/lulivi/search5bot",
   packages=['search5bot'],
   install_requires=['unittest', 'decouple', 'yandex_search'],
)
