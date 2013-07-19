Creating a gist
===============

.. warning::

	user must be authenticated 

.. note::

	Input

		``name``
		  *Optional* argument (*default auto-gistID*)
		``description``
		  *Optional* argument (*default empty*)
		``public``
		  *Optional* argument (*default public*)
		``content``
		  *Required* argument


Creating a Gist with all arguments ``create(params)``
-----------------------------------------------------

Create a new Gist simply by providing the parameters as specified above.

.. code-block:: python

	# create a secret gist(public=0)
	GHgist.create(name='_GISTNAME', description='_ANY_DESCRIPTION', public=0, content='_CONTENT_GOES_HERE')

Creating a Gist with *required* argument only ``create(params)``
----------------------------------------------------------------

.. code-block:: python
	
	# create a gist with defaut name(gist:gistID, provided by github)
	GHgist.create(content='_CONTENT_GOES_HERE')

Other docs
^^^^^^^^^^

* :doc:`index`
* :doc:`manage`
* :doc:`actions` 
* :doc:`searching`
* :doc:`comments`
