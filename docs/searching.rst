Search User's gists
===================

Listing all the Gists ``search('_USERNAME').listall()``
-------------------------------------------------------

Fetch all the GistsNames of a Github User.

.. note::

	Only recent 30 gists will be shown as per the Github API v3

.. code-block:: python

	GHgist.search('_USERNAME').listall()

Listing the required number of Gists ``search('_USERNAME').list(integer)``
--------------------------------------------------------------------------

Fetch only the limited number of Gists.

.. note::

	Input

		integer
			``integer`` is **required** as an argument which will limit the number of Gists to be listed.

.. code-block:: python

	GHgist.search('_USERNAME').list(2)

Fetching the contents of a Gist using GistName ``search('_USERNAME').content(params)``
--------------------------------------------------------------------------------------

Fetch the contents of a Gist by name (GistName).

.. code-block:: python

	GHgist.search('_USERNAME').content(name='_GISTNAME')

Fetching the contents of any Gist using GistID ``search('').content(id='_GISTID')``
-----------------------------------------------------------------------------------

Fetch by id (GistID)

.. code-block:: python

	GHgist.search('').content(id='_GISTID')

Fetch GistName ``search('').getgist(id='_GISTID')``
---------------------------------------------------

Fetch Gist's name by provoding it's ID i.e. GistID.

.. code-block:: python

	GHgist.search('').getgist(id='_GISTID')

Fetch Gist-Link, Clone-Link and Embed-Script-Link of searched gist ``search('_USERNAME/EMPTY').links(id/name)``
------------------------------------------------------------------------------------------------------------------------------

It is very very useful and solves the dual purpose. Providing the username and a Gistname of that user not only provides the above mentioned Links but also let 'one' know about the GistID of that Gist.

Moreover, this criteria can also be applied in finding 'one\'s' own Gist's GistID by providing Gistname.

.. note::

	Input

		``name/id`` -
					  if providing GistdID, Github-Username should be blank like 	search(''),links(id='_GISTID')
					  if providing GistName, Github-Username is required like search('Github-User').links(name='THATUSERSGISTNAME')

			*Required*

.. code-block:: python

	GHgist.search('').links(id='_GISTID')
	GHgist.search('_USERNAME').links(name='_GISTNAME')

Other Docs
^^^^^^^^^^

* :doc:`index`
* :doc:`create`
* :doc:`manage`
* :doc:`actions`
* :doc:`comments`
