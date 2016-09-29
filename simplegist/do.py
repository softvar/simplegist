import json
import requests
from config import BASE_URL, GIST_URL

class Do:
	def __init__(self, gist):
		self.gist = gist

	def getMyID(self,gist_name):
		'''
		Getting gistID of a gist in order to make the workflow
		easy and uninterrupted.
		'''
		r = requests.get(
			'%s'%BASE_URL+'/users/%s/gists' % self.gist.username,
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

	def star(self, **args):
		'''
		star any gist by providing gistID or gistname(for authenticated user)
		'''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid to be starred')

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
		'''
		unstar any gist by providing gistID or gistname(for authenticated user)
		'''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid to be unstarred')

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
		'''
		fork any gist by providing gistID or gistname(for authenticated user)
		'''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid to be forked')

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
		'''
		Check a gist if starred by providing gistID or gistname(for authenticated user)
		'''

		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid to be checked for star')

		r = requests.get(
			'%s'%BASE_URL+'/gists/%s/star' % self.gist_id,
			headers=self.gist.header
			)
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