import os
from setuptools import setup
from codecs import open


def read(filename):
    with open(filename, 'r', 'utf-8') as f:
        readme = f.read()
    return readme

setup(
    name="pumpy",
    version="0.0.1",
    author="Finn Aarup Nielsen",
    author_email="faan@dtu.dk",
    description="A demonstration of pure Python matrix library",
    license="GPL",
    keywords="matrix numerical",
    url="https://github.com/fnielsen/pumpy",
    packages=['pumpy', 'pumpy.test', 'examples'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
)
