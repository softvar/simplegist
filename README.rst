GistApi-Wrapper-python
======================

Python wrapper for ``GitHub's Gist``.

Features
--------

* Creating gists returning the url, script and clone link for copy-paste purpose
* Checkout one's gists - Name(s), Description and Content
* Edit and Delete a gist
* Search GitHub user's gist - fork, star and unstar them
* List-all comments of any gist, make/edit a comment on a gist, delete a comment 

Installation
-------------
.. code-block:: bash

    $ pip install gists

Example Usage
-------------

.. code-block:: python

    from gist import Gist

    GHgist = Gist(username='USERNAME',api_token='API_TOKEN') 
    # or provide USERNAME and API_TOKEN in config.py file, so just, GHgist = Gist()

    # creating gist and returning url, script, clone link
    GHgist.create(name='Test.py', description='just testing it', public=1, content='print "Yay! Test Passed" ') 

    # Lists all the names of authenticated user's gists
    GHgist.profile().listall()

    # Lists only the names of recent two gists of user 'softvar' 
    GHgist.search('geojeff').list(2)
    
    # Lists all the comments on gist named 'bootstrap-min.css' of user 'softvar'
    GHgist.comments().listall(user='softvar',name='bootstrap-min.css')

    # ...and many more...

Patches and suggestions are welcomed
------------------------------------

.. code-block:: bash
   $ git clone 