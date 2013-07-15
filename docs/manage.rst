Managing authenticated user's gists
==================================

.. warning::

	user must be authenticated 


Listing all the Gists
---------------------

.. note::

	Only recent 30 gists will be shown as per the Github API v3

.. code-block:: python

	GHgist.profile().listall()

Listing the required Gists
--------------------------
Fetch only the limited number of Gists

.. note::

	``Input``

		integar
			``integar`` is **required** as an argument which will limit the number of Gists to be listed.

.. code-block:: python

	GHgist.profile().list(4)
	
Fetching the contents of a Gist
-------------------------------

Fetch by name (GistName)

.. code-block:: python

	GHgist.profile().content(name='bootstrap-min.css')
	
Fetch by id (GistID)

.. code-block:: python

	GHgist.profile().content(id='5948962')

Listing the starred Gists
-------------------------

List all your starred gists

.. code-block:: python

	GHgist.profile().starred()

List only the required number of starred Gists

.. note::

	**limit**
		*Required*

.. code-block:: python

	GHgist.profile().starred(limit=1)

	 