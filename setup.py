from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='pranali_reloaded',
    version=version,
    description='A reporting system for Rotaract District Organization',
    author='Rotaract 3141',
    author_email='admin@rotaract3141.org',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
