
import sys
from distutils.core import setup

required = ['requests']


if sys.version_info[:2] < (2,6):
    required.append('simplejson')

    setup(
        name = 'gist',
        packages = ['gist'], 
        version = '0.1',
        install_requires=required,
        description = 'Python wrapper for Gist ',
        long_description=open('README.rst').read(),
        author = 'Varun Malhotra',
        author_email = 'varun2902@gmail.com',
        url = 'https://github.com/softvar/gist', 
        download_url = 'https://github.com/softvar/GistApi-Wrapper-python/tarball/0.1',        keywords = ['gist', 'github', 'API'], # arbitrary keywords
        license = 'MIT', 
        classifiers = [],
    )