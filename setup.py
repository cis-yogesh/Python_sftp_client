#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name = "Python sftp",
    version = "0.2",
    py_modules = ['sftp',],

    install_requires = ['paramiko>=1.7.4'],

    package_data = {
        '': ['README','*.txt', '*.rst'],
    },
    author = "yogesh dwivedi",
    author_email = "yogesh.p@cisinlabs.com",
    description = "Python module for SFTP Client",
    license = "BSD",
    keywords = "python django sftp ftp",
    url = "",
    long_description = "SFTP Client for Python",
    platforms=['Linux, Windows'],
    download_url='',
)
