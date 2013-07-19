GistAPI for Comments Section 
============================


Listing all the comments on your Gists ``comments().listall(params)``
---------------------------------------------------------------------

List all the contents of comments made on a single Gist by providing the GistName/GistID and USERNAME if the gist is not yours.

.. note::

	Input
		``user`` - for listing out the comments on a Gist of *some* user.
			Optional

Fetch all the comments on a Gist ``listall(name='*gistname*')`` ``listall(id='*gistid*')``.

.. code-block:: python

	# listing comments on your gist = *GISTNAME*
	GHgist.comments().listall(name='GISTNAME')

.. code-block:: python

	# listing comments on a gist of user = *GITHUBUSERNAME*
	GHgist.comments().listall(user='GITHUBUSERNAME', name='GISTNAME')

Fetch a single comment on a Gist ``comments().get(params)``
-----------------------------------------------------------

Fetch any comment's contents just by providing it's GistName/GistID along with the CommentID.

.. note::

	Input
		
		``name/id`` - GistName/GistID
			*Required*
		``commentid`` - commentid of a comment
			*Required*

.. code-block:: python

	GHgist.comments().get(name='bootstrap-min.css', commentid='862438')

Post/Create a comment on a Gist ``comments().create(params)``
-------------------------------------------------------------

Post a comment on a Gist providing GistName/GistID, BODY of Comment and USERNAME.
Commenting on your own Gist doesn't require USERNAME as an argument.

.. note::

	Input
	
		``name/id`` - GistName/GistID
			*Required*
		``body`` - contents of a comment to be posted
			*Required*
		``user`` - comment on a Github user's gist
			*Optional* if commenting on your Gist only
			*Required* if commenting on others Gist

.. code-block:: python

	# commenting on your own Gist with id='*GISTID*' and body='*CONTENTS_OF_COMMENT*'
	GHgist.comments().create(id='5948962', body='hello')

	# commenting on Github user = '*USERNAME*' with name='*GISTNAME*' with body='*CONTENTS_OF_COMMENT*'
	GHgist.comments().create(user='caspyin',name='curl.md', body='very helpful')

Edit a comment on a Gist ``comments().edit(params)``
----------------------------------------------------

Edit Body of any comment on a Gist by providing GistName/GistID, commentID, BODY to be edited and USERNAME (if the Gist is not yours).

.. note::

	Input
		name/id - GistName/GistID
			*Required*
		commentid - commentid of a comment
			*Required*
		body - contents of a comment to be posted
			*Required*
		user - comment on a Github user's gist
			*Optional* if commenting on your Gist only
			*Required* if commenting on others Gist

.. code-block:: python

	GHgist.comments().edit(name='bootstrap-min.css', commentid='862438',body='heya! world')

Delete a comment on a GIst ``comments().delete(params)``
--------------------------------------------------------

Delete any comment you have made on a Gist by provoding GistName/GistID along with commentID.

.. warning::
	user must be authenticated

.. note::

	Input
		name/id - GistName/GistID
			*Required*
		commentid - commentid of a comment
			*Required*

.. code-block:: python

	GHgist.comments().delete(name='bootstrap-min.css', commentid='862454')

Other docs
^^^^^^^^^^

* :doc:`index`
* :doc:`create`
* :doc:`manage`
* :doc:`actions`
* :doc:`searching`
