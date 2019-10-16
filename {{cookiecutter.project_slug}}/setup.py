#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.in') as requirements_file:
     requirements = requirements_file.read()

setup(
    name="{{cookiecutter.project_slug}}",
    packages=find_packages(),
    install_requires=requirements,
    version="{{cookiecutter.version}}",
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name }}",
)
