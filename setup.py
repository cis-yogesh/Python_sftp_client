# setup.py file
from setuptools import setup, find_packages
setup(
    name = "django_sftp",
    version = "0.1",
    py_modules = ['django_sftp',],

    install_requires = ['paramiko>=1.7.4','pysftp>=0.2.2','Django >=1.4'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['README','*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author = "yogesh dwivedi",
    author_email = "yogeshd.mca@gmail.com",
    description = "Connect django from sftp using paramiko and google sftp module",
    license = "BSD",
    keywords = "django sftp",
    url = "",
    long_description = "Sftp module for Django >1.4",
    platforms=['any'],
    download_url='',
)
