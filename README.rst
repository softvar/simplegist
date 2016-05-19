Github-Gist Api - python wrapper
================================

Python wrapper for ``GitHub's Gist API``.

|Latest Version| |Downloads|

.. |Latest Version| image:: https://img.shields.io/pypi/v/simplegist.svg
    :target: https://pypi.python.org/pypi/simplegist

.. |Downloads| image:: https://img.shields.io/pypi/dm/simplegist.svg
    :target: https://pypi.python.org/pypi/simplegist

Features
--------

* Create Gists and get url, script and clone link on success (can be used for copy-paste purpose too)
* View one's Gist(s) - name, description and it's content
* Edit and Delete a gist
* Search Gist(s) of any user; fork, star and unstar them
* List all comments on any Gist, put/edit/delete a comment on a Gist

Installation
-------------
.. code-block:: bash

    $ pip install simplegist

Download `here <https://github.com/softvar/simplegist/tarball/1.0.0>`_ and run ``python setup.py install`` after changing directory to ``/simplegist``

Generating Github API Access Token
----------------------------------
Go to Github's Account settings > Applications
``Create a new token`` and use it for making API requests instead of password

Example Usage
-------------

.. code-block:: python

    from simplegist import Simplegist

    ghGist = Simplegist(username='USERNAME', api_token='API_TOKEN')
    # or provide USERNAME and API_TOKEN in config.py file, so just, ghGist = Gist()

    # creating gist and getting url, script and clone link
    ghGist.create(name='_GISTNAME', description='_ANY_DESCRIPTION', public=1, content='_CONTENT_GOES_HERE')

    # List down all the names of authenticated user's Gists
    ghGist.profile().listall()

    # List down only the names of recent two Gists of user '_USERNAME'
    ghGist.search('_USERNAME').list(2)

    # List down all the comments on gist named '_GISTNAME' of user 'USERNAME'
    ghGist.comments().listall(user='_USERNAME', name='_GISTNAME')

    # ...and many more...

Full Usage and Documentation
----------------------------

Visit here `READTHEDOCS <https://simplegist.readthedocs.org/en/latest/>`_ or `PYTHONHOSTED <http://pythonhosted.org/simplegist/>`_

Patches and suggestions are welcome
-----------------------------------

.. code-block:: bash

   $ git clone https://github.com/softvar/simplegist.git
   $ cd simplegist
