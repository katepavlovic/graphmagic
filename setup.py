#!/usr/bin/env python

from setuptools import find_packages
from setuptools import setup


def find_subpackages(package):
    packages = [package]
    for subpackage in find_packages(package):
        packages.append("{0}.{1}".format(package, subpackage))
    return packages


setup(name="graphmagic",
      version="0.1",
      description="Perform operations with graphs",
      url="https://github.com/katepavlovic/graphmagic",
      author="Kate Pavlovic",
      author_email="ekpavlovic@gmail.com",
      packages=find_subpackages("graphmagic"),
      platforms='any',
      license='Apache 2.0',
      entry_points={
          "console_scripts": ["graphmagic = graphmagic.main:main",],
      })
