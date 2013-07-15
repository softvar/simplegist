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

Contents:
---------

.. toctree::
   :maxdepth: 2

   create
   manage
   search
   comments

Installation
-------------
.. code-block:: bash

    $ pip install simplegist

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

.. code-block:: python

    from simplegist import SimpleGist

    GHgist = Simplegist(username='USERNAME',api_token='API_TOKEN') 
    # or provide USERNAME and API_TOKEN in config.py file, so just, GHgist = Gist()

    # creating gist and returning url, script, clone link
    GHgist.create(name='Test.py', description='just testing it', public=1, content='print "Yay! Test Passed" ') 

    # Lists all the names of authenticated user's gists
    GHgist.profile().listall()

    # Lists only the names of recent two gists of user 'softvar' 
    GHgist.search('softvar').list(2)
    
    # Lists all the comments on gist named 'bootstrap-min.css' of user 'softvar'
    GHgist.comments().listall(user='softvar',name='bootstrap-min.css')

    # ...and many more...

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

