import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="pumpy",
    version="0.0.1",
    author="Finn Aarup Nielsen",
    author_email="faan@dtu.dk",
    description=("An demonstration of pure Python matrix library"),
    license="GPL",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['pumpy', 'pumpy.core', 'pumpy.core.test', 'examples'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
