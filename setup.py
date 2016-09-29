
import sys
from setuptools import setup

required = ['requests']


if sys.version_info[:2] < (2,6):
    required.append('simplejson')

setup(
    name = 'simplegist',
    packages = ['simplegist'],
    version = '1.0.1',
    install_requires=required,
    description = 'Python wrapper for Gist ',
    long_description=open('README.rst').read(),
    author = 'Varun Malhotra',
    author_email = 'varun2902@gmail.com',
    url = 'https://github.com/softvar/simplegist',
    download_url = 'https://github.com/softvar/simplegist/tarball/1.0.1',
    keywords = ['gist', 'github', 'API'],
    license = 'MIT',
    classifiers = (
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ),
)