BASE_URL = 'https://api.github.com'
GIST_URL = 'https://gist.github.com'

import json
import requests



class Do:
	def __init__(self, gist):
		self.gist = gist

	def star(self, **args):
		
		if 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Provide GistID to be starred')

		r = requests.put(
			'%s'%BASE_URL+'/gists/%s/star' % self.gist_id,
			headers=self.gist.header
			)
		if (r.status_code == 204):
			response = {
				'id': self.gist_id
			}
			return response

		raise Exception('Gist can\'t be starred')

	def unstar(self, **args):
		
		if 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Provide GistID to be unstarred')

		r = requests.delete(
			'%s'%BASE_URL+'/gists/%s/star' % self.gist_id,
			headers=self.gist.header
			)
		if (r.status_code == 204):
			response = {
				'id': self.gist_id
			}
			return response

		raise Exception('Gist can\'t be unstarred')

	def fork(self, **args):

		if 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Provide GistID to be forked')

		r = requests.post(
			'%s'%BASE_URL+'/gists/%s/forks' % self.gist_id,
			headers=self.gist.header
			)
		if (r.status_code == 201):
			response = {
				'id': self.gist_id,
				'description': r.json()['description'],
				'public': r.json()['public'],
				'comments': r.json()['comments']
			}
			return response

		raise Exception('Gist can\'t be forked')

	def checkifstar(self, **args):

		if 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Provide GistID to be forked')

		r = requests.get(
			'%s'%BASE_URL+'/gists/%s/star' % self.gist_id,
			headers=self.gist.header
			)
		print r.status_code
		if (r.status_code == 204):
			response = {
				'starred': 'True',
				'id': self.gist_id
				}
		else:
			response = {
				'starred': 'False'
			}

		return response