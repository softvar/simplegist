Managing authenticated user's gists
==================================

.. warning::

	user must be authenticated 


Listing all the Gists
---------------------

Fetch all the GistsNames ``listall()``.

.. note::

	Only recent 30 gists will be shown as per the Github API v3

.. code-block:: python

	GHgist.profile().listall()

Listing the required Gists
--------------------------

Fetch only the limited number of Gists ``list(4)``.

.. note::

	``Input``

		integar
			``integar`` is **required** as an argument which will limit the number of Gists to be listed.

.. code-block:: python

	GHgist.profile().list(4)
	
Fetching the contents of a Gist
-------------------------------

Fetch the contents of a Gist by name (GistName) ``content(name='Gistname')``.

.. code-block:: python

	GHgist.profile().content(name='GISTNAME')
	
Fetch by id (GistID)

.. code-block:: python

	GHgist.profile().content(id='GistID')

Listing the starred Gists
-------------------------

List all your starred gists ``starred()``

.. code-block:: python

	GHgist.profile().starred()

List only the required number of starred Gists ``starred(limit=2)``.

.. note::

	**limit**
		*Required*

.. code-block:: python

	GHgist.profile().starred(limit=2)

Editing a Gist
--------------

Edit a Gist by providing either GistName or GistID, and content.

.. note::

	Input
		description
			*Optional*
		name or id
			*Required*
		content
			*Required*


.. code-block:: python

	# with all the arguments
	GHgist.profile().edit(description='NEW UPDATE',name='GISTNAME',content='MY UPDATED GIST ')

	# with required arguments
	GHgist.profile().edit(id='GistID',content='MYUPDATED GIST ')	

Getting a GistName using GistID
-------------------------------

Very useful in order to work hasslefree ``getMyID('YOUR_GIST_NAME')``.

.. code-block:: python

	GHgist.profile().getMyID('YOUR_GIST_NAME')



Deleting a Gist
---------------

Delete a gist by providing either GistName or GistID ``delete(id='GistID')``.

.. note::

	Input
		name or id
			*Required*

.. code-block:: python

	Ghgist.profile().delete(id=':GistID')


	 