Creating a gist
===============

.. warning::

	user must be authenticated 

.. note::

	Input

		name
		  *Optional* argument (*default auto-gistID*)
		description
		  *Optional* argument (*default empty*)
		public
		  *Optional* argument (*default true*)
		content
		  *Required* argument


Creating a Gist with all arguments
----------------------------------

.. code-block:: python

	# create a secret gist(public=0)
	GHgist.create(name='Test.py', description='just testing it', public=0, content='print "Yay! Test Passed" ')

Creating a Gist with *required* argument only
---------------------------------------------

.. code-block:: python
	
	# create a gist with defaut name(gist:gistID, provided by github)
	GHgist.create(content='print "Yay! Test Passed" ') 