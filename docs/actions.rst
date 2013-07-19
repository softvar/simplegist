Actions on gists
================

.. warning::

	user must be authenticated

Useful Information for below mentioned methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since all the below mentioned methods require GistName/GistID. GistName is provided only when calling methods for your own Gists. Whereas GistID can be provided for all.

**GistID of other users' Gist can be easily extracted without opening browser. Refer to the**
:doc:`searching` **section** 

Check a Gist for a star ``do().checkifstar(params)``
----------------------------------------------------

Check any Gist for a star by providing Gistname(if that Gist belongs to you) or GistID.


.. note::

	Input

		``name/id``
				  provide **name** only if that gist belongs to you
				  , provide **id** for checking correspondong Gist 

				*Required*

.. code-block:: python

	GHgist.do().checkifstar(id='_GISTID')

	# provide your Gistname
	GHgist.do().checkifstar(name='_YOUR_GISTNAME')

Star a Gist ``do().star(params)``
---------------------------------

Star any Gist by providing Gistname(if that Gist belongs to you) or GistID.


.. note::

	Input

		``name/id``
				  provide **name** only if that gist belongs to you
				  , provide **id** for starring corresponding Gist 

			*Required*

.. code-block:: python

	GHgist.do().star(id='_GISTID')

	# provide your Gistname
	GHgist.do().star(name='_YOUR_GISTNAME')

Unstar a Gist ``do().unstar(params)``
-------------------------------------

UnStar any Gist by providing Gistname(if that Gist belongs to you) or GistID.


.. note::

	Input

		``name/id``

			provide **name** only if that gist belongs to you
			, provide **id** for unstarring corresponding Gist 
		
			*Required*

.. code-block:: python
	
	GHgist.do().unstar(id='_GISTID')

	# provide your Gistname
	GHgist.do().unstar(name='_YOUR_GISTNAME')  

Fork a Gist ``do().fork(params)``
---------------------------------

Fork other's Gist by providing GistID.


.. note::

	Input

		``id``
		   	  provide **id** for forking corresponding Gist 
		
			*Required*

.. code-block:: python

	GHgist.do().fork(id='_GISTID')

Other Docs
^^^^^^^^^^

* :doc:`index`
* :doc:`create`
* :doc:`manage`
* :doc:`searching`
* :doc:`comments`