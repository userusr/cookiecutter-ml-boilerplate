from setuptools import find_packages, setup

setup(
    name='{{cookiecutter.project_slug}}',
    packages=find_packages(),
    version='{{cookiecutter.version}}',
    description='{{ cookiecutter.project_short_description }}',
    author='{{ cookiecutter.full_name }}'
)
