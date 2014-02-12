Github-Gist Api - python wrapper
================================

Python wrapper for ``GitHub's Gist API``.

|Latest Version| |Downloads|

.. |Latest Version| image:: https://pypip.in/v/simplegist/badge.png
    :target: https://pypi.python.org/pypi/simplegist/

.. |Downloads| image:: https://pypip.in/d/simplegist/badge.png
    :target: https://pypi.python.org/pypi//simplegist/


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

Download `here <https://github.com/softvar/simplegist/tarball/0.3.2>`_ and run ``python setup.py install`` after changing directory to ``/simplegist``

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
    GHgist.create(name='_GISTNAME', description='_ANY_DESCRIPTION', public=1, content='_CONTENT_GOES_HERE') 

    # Lists all the names of authenticated user's gists
    GHgist.profile().listall()

    # Lists only the names of recent two gists of user '_USERNAME' 
    GHgist.search('_USERNAME').list(2)
    
    # Lists all the comments on gist named '_GISTNAME' of user 'USERNAME'
    GHgist.comments().listall(user='_USERNAME',name='_GISTNAME')

    # ...and many more...

Full Usage and Documentation
----------------------------

Visit here `READTHEDOCS <https://simplegist.readthedocs.org/en/latest/>`_ or `PYTHONHOSTED <http://pythonhosted.org/simplegist/>`_

Patches and suggestions are welcomed
------------------------------------

.. code-block:: bash

   $ git clone https://github.com/softvar/simplegist.git
   $ cd simplegist
