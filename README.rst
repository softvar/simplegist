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

    $ pip install simplegist

Generating Github API Access Token
----------------------------------
Go to Github's Account settings > Applications
``Create a new token`` and use it for making API requests instead of password

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

Full Usage and Documentation
----------------------------

Visit here `READTHEDOCS <https://simplegist.readthedocs.org/en/latest/>`

Patches and suggestions are welcomed
------------------------------------

.. code-block:: bash

   $ git clone https://github.com/softvar/GistApi-Wrapper-python.git
   $ cd GistApi-Wrapper-python