
import sys
from distutils.core import setup

required = ['requests']


if sys.version_info[:2] < (2,6):
    required.append('simplejson')

    setup(
        name = 'gist',
        packages = ['gist'], # this must be the same as the name above
        version = '0.1',
        install_requires=required,
        description = 'Python wrapper for Gist ',
        long_description=open('README.rst').read(),
        author = 'Varun Malhotra',
        author_email = 'varun2902@gmail.com',
        url = 'https://github.com/softvar/gist',   # use the URL to the github repo
        download_url = 'https://github.com/softvar/gist/tarball/0.1', # I'll explain this in a second
        keywords = ['gist', 'github', 'API'], # arbitrary keywords
        license = 'MIT', 
        classifiers = [],
    )