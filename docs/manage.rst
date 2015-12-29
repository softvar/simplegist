Managing authenticated user's gists
===================================

.. warning::

	user must be authenticated


Listing all the Gists ``profile().listall()``
---------------------------------------------

Fetch all the GistsNames.

.. note::

	Only recent 30 gists will be shown as per the Github API v3

.. code-block:: python

	GHgist.profile().listall()

Listing the required number of Gists ``profile().list(integer)``
----------------------------------------------------------------

Fetch only the limited number of Gists ``list(4)``.

.. note::

	Input

		integer
			``integer`` is **required** as an argument which will limit the number of Gists to be listed.

.. code-block:: python

	GHgist.profile().list(4)

Get GistName ``profile().getgist(id='_GISTID')``
------------------------------------------------

Fetch Gist's name by provoding it's ID i.e. GistID.

.. code-block:: python

	GHgist.profile().getgist(id='_GISTID')

Fetch Gist-Link, Clone-Link and Embed-Script-Link of your gist ``profile().links(id/name)``
-------------------------------------------------------------------------------------------

.. note::

	Input

		``name/id`` - id should be correct so check response before using 				 	  it further.
			*Required*

.. code-block:: python

	GHgist.profile('YOURUSERNAME').links(id='_GISTID')
	GHgist.profile('YOURUSERNAME').links(name='_GISTNAME')

Fetching the contents of a Gist ``profile().content(params)``
-------------------------------------------------------------

Fetch the contents of a Gist by name (GISTNAME) ``content(name='_GISTNAME')``.

.. code-block:: python

	GHgist.profile().content(name='_GISTNAME')

Fetch by id (GISTID)

.. code-block:: python

	GHgist.profile().content(id='_GISTID')

Listing the starred Gists ``profile().starred()``
-------------------------------------------------

List all your starred gists ``starred()``

.. code-block:: python

	GHgist.profile().starred()

List only the required number of starred Gists ``starred(limit=2)``.

.. note::

	``limit``
		*Required*

.. code-block:: python

	GHgist.profile().starred(limit=2)

Get GistName ``profile().getgist(id='_GISTID')``
------------------------------------------------

Fetch any of your Gist's name by provoding it's ID i.e. GISTID.

.. code-block:: python

	GHgist.profile().getgist(id='_GistID')

Editing a Gist ``profile().edit(params)``
-----------------------------------------

Edit a Gist by providing either GistName or GistID, and content.

.. note::

	Input

		``description``
			*Optional*
		``name/id``
			*Required*
		``content``
			*Required*


.. code-block:: python

	# with all the arguments
	GHgist.profile().edit(description='_NEW_DESCRIPTION',name='_GISTNAME',content='_UPDATED_CONETNT_GOES_HERE')

	# with required arguments
	GHgist.profile().edit(id='_GISTID',content='_UPDATED_CONTENT_GOES_HERE')

Getting a GistName using GistID ``profile().getMyID(params)``
-------------------------------------------------------------

Very useful in order to work hasslefree ``getMyID('_YOUR_GIST_NAME')``.

.. code-block:: python

	GHgist.profile().getMyID('_YOUR_GIST_NAME')



Deleting a Gist ``profile().delete(params)``
--------------------------------------------

Delete a gist by providing either GistName or GistID ``delete(id='_GISTID')``.

.. note::

	Input
		``name/id``
			*Required*

.. code-block:: python

	GHgist.profile().delete(id='_GISTID')

Other Docs
^^^^^^^^^^

* :doc:`index`
* :doc:`create`
* :doc:`actions`
* :doc:`searching`
* :doc:`comments`