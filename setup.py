"""Setup file."""

# external imports
from setuptools import setup, find_packages

long_description = ''
with open("README.md", 'r') as f:
    long_description = f.read()

version = {}
with open('search_5_bot/version.py') as fp:
    exec(fp.read(), version)

requirements = [
    'python-decouple', 'yandex_search', 'requests', 'lxml'
]

non_packages = ['contrib', 'docs', 'tests', 'data']

setup(
    name='search5bot',
    version=version['__version__'],
    description='A telegram search bot',
    long_description=long_description,
    license="GPLv3",
    author='Jorge Chamorro, Luis Liñán',
    author_email='jorge@jorgechp.com, luislivilla@gmail.com',
    url="https://github.com/lulivi/search5bot",
    packages=find_packages(exclude=non_packages),
    install_requires=requirements, )
