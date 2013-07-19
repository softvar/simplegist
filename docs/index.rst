.. simplegist documentation master file, created by
   sphinx-quickstart on Mon Jul 15 12:56:40 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to simplegist's documentation!
======================================
Helps in carrying out easy workflow for maintaining gists

Features
--------

* Creating gists returning the url, script and clone link for copy-paste purpose
* Checkout one's gists - Name(s), Description and Content
* Edit and Delete a gist
* Search GitHub user's gist - fork, star and unstar them
* List comments of any gist, make/edit a comment on a gist, delete a comment 

Installation
------------
.. code-block:: bash

    $ pip install simplegist

Or download it from `here <https://github.com/softvar/GistApi-Wrapper-python/tarball/0.3.2>`_ and then,

.. code-block:: bash

    $ cd /to/this/directory/
    $ python install setup.py

Generating Github API Access Token
----------------------------------

Go to Github's Account settings > Applications
``Create a new token`` and use it for making API requests instead of password.

Creating an Instance
---------------------

.. code-block:: python

	# if USERNAME and API_TOKEN are not provided in config.py
	GHgist = Simplegist(username='USERNAME',api_token='API_TOKEN')

	# else
	GHgist = Simplegist() 

Example Usage
-------------
Below is an example to getting started with using GistAPI and its useful functionalities.


.. code-block:: python

    from simplegist import SimpleGist

    # provide USERNAME and API_TOKEN in config.py file, so just, GHgist = Gist(), OR,
    GHgist = Simplegist(username='USERNAME',api_token='API_TOKEN') 

    # creating gist and returning url, script, clone link
    GHgist.create(name='_GISTNAME', description='_ANY_DESCRIPTION', public=1, content='_CONTENT_GOES_HERE') 

    # Lists all the names of authenticated user's gists
    GHgist.profile().listall()

    # Lists only the names of recent two gists of user '_USERNAME' 
    GHgist.search('_USERNAME').list(2)
    
    # Lists all the comments on gist named '_GISTNAME' of user '_USERNAME'
    GHgist.comments().listall(user='_USERNAME',name='_GISTNAME')

    # ...and many more...

Contents:
---------

.. toctree::
   :maxdepth: 2

   create
   manage
   actions
   searching
   comments

Other docs
==========

* :doc:`create`
* :doc:`manage`
* :doc:`actions`
* :doc:`searching`
* :doc:`comments`
