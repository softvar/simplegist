import json
import requests
from config import BASE_URL, GIST_URL

class Comments:
	def __init__(self, gist):
		self.gist = gist


	def getMyID(self,gist_name):
		'''
		Getting gistID of a gist in order to make the workflow
		easy and uninterrupted.
		'''
		r = requests.get(
			'%s'%BASE_URL+'/users/%s/gists' % self.user,
			headers=self.gist.header
			)
		if (r.status_code == 200):
			r_text = json.loads(r.text)
			limit = len(r.json())

			for g,no in zip(r_text, range(0,limit)):
				for ka,va in r.json()[no]['files'].iteritems():
					if str(va['filename']) == str(gist_name):
						return r.json()[no]['id']
			return 0

		raise Exception('Username not found')


	def listall(self, **args):
		if 'user' in args:
			self.user = args['user']

		else:
			self.user = self.gist.username

		self.gist_name = ''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid')

		if self.gist_id:
			allcomments = []
			r = requests.get(
				'%s'%BASE_URL+'/gists/%s/comments' % self.gist_id,
				headers=self.gist.header
			)
			r_text = json.loads(r.text)
			limit = len(r.json())
			if (r.status_code == 200 ):
				for g,no in zip(r_text, range(0,limit)):
						allcomments.append(r.json()[no]['body'])

				return allcomments

		raise Exception('Gistname not found')

	def create(self, **args):
		if 'body' in args:
			self.body = {'body':args['body']}
		else:
			raise Exception('Comment Body can\'t be empty')
		if 'user' in args:
			self.user = args['user']

		else:
			self.user = self.gist.username

		self.gist_name = ''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid')

		if self.gist_id:

			r = requests.post(
				'%s'%BASE_URL+'/gists/%s/comments' % self.gist_id,
				headers=self.gist.header,
				data=json.dumps(self.body)
			)
			if (r.status_code == 201):
				response ={
					'GistID': self.gist_id,
					'CommenID': r.json()['id'],
					'body': self.body['body'],
					'created_at': r.json()['created_at']
				}
				return response


		raise Exception('Comment not created')


	def delete(self, **args):

		self.user = self.gist.username

		self.gist_name = ''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid')

		if 'commentid' in args:
			self.commentid = args['commentid']
		else:
			raise Exception('CommenID not provided')

		if self.gist_id:
			r = requests.delete(
				'%s/gists/%s/comments/%s'%(BASE_URL,self.gist_id, self.commentid),
				headers=self.gist.header
			)
			if (r.status_code == 204):
				response ={
					'deleted': 'True',
					'GistID': self.gist_id,
					'CommentID': self.commentid,
				}
				return response
			else:
				response ={
					'comment' : 'not exists'
				}
				return response

		raise Exception('Gist/Comment not exits')


	def get(self, **args):

		self.user = self.gist.username

		self.gist_name = ''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid')

		if 'commentid' in args:
			self.commentid = args['commentid']
		else:
			raise Exception('CommenID not provided')

		if self.gist_id:
			r = requests.get(
				'%s/gists/%s/comments/%s'%(BASE_URL,self.gist_id, self.commentid),
				headers=self.gist.header
			)
			if (r.status_code == 200):
				response ={
					'body': r.json()['body'],
					'GistID': self.gist_id,
					'CommentID': self.commentid,
					'created_at': r.json()['created_at']
				}
				return response
			else:
				response ={
					'comment' : 'not exists'
				}
				return response


		raise Exception('Comment not exits/deleted')

	def edit(self, **args):
		if 'body' in args:
			self.body = {'body':args['body']}
		else:
			raise Exception('Comment Body can\'t be empty')
		if 'user' in args:
			self.user = args['user']

		else:
			self.user = self.gist.username

		if 'commentid' in args:
			self.commentid = args['commentid']
		else:
			raise Exception('CommenID not provided')

		self.gist_name = ''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid')

		if self.gist_id:

			r = requests.patch(
				'%s/gists/%s/comments/%s'%(BASE_URL,self.gist_id, self.commentid),
				headers=self.gist.header,
				data=json.dumps(self.body)
			)
			if (r.status_code == 200):
				response ={
					'GistID': self.gist_id,
					'CommenID': r.json()['id'],
					'body': self.body['body'],
					'created_at': r.json()['created_at']
				}
				return response
			else:
				response = {
					'comment' : 'not edited'
				}


		raise Exception('Comment not edited')