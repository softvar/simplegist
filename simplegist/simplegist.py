import requests
import json

from config import USERNAME, API_TOKEN, BASE_URL, GIST_URL

from mygist import Mygist
from do import Do
from comments import Comments

class Simplegist:
	"""
	Gist Base Class

	This class is to used to instantiate the wrapper and authenticate.

	Authenticate with providing Github Username and API-Token to use
	it for all future API requests
	"""

	def __init__(self, **args):
		# Save our username and api_token (If given) for later use.
		if 'username' in args:
			self.username = args['username']
		else:
			if not USERNAME:
				raise Exception('Please provide your Github username.')
			else:
				self.username = USERNAME

		if 'api_token' in args:
			self.api_token = args['api_token']
		else:
			if not API_TOKEN:
				raise Exception('Please provide your Github API Token.')
			else:
				self.api_token = API_TOKEN


        # Set header information in every request.
		self.header = { 'X-Github-Username': self.username,
						'Content-Type': 'application/json',
						'Authorization': 'token %s' %self.api_token
					  }

	def profile(self):
		return Mygist(self)

	def search(self, user):
		return Mygist(self,user=user)

	def do(self):
		return Do(self)

	def comments(self):
		return Comments(self)

	def create(self, **args):
		if 'description' in args:
			self.description = args['description']
		else:
			self.description = ''

		if 'name' in args:
			self.gist_name = args['name']
		else:
			self.gist_name = ''

		if 'public' in args:
			self.public = args['public']
		else:
			self.public = 1

		if 'content' in args:
			self.content = args['content']
		else:
			raise Exception('Gist content can\'t be empty')

		url = '/gists'

		data = {"description": self.description,
  				"public": self.public,
  				"files": {
    				self.gist_name: {
      				"content": self.content
    				}
  				}
  		}

		r = requests.post(
			'%s%s' % (BASE_URL, url),
			data=json.dumps(data),
			headers=self.header
		)
		if (r.status_code == 201):
			response = {
			'Gist-Link': '%s/%s/%s' %(GIST_URL,self.username,r.json()['id']),
			'Clone-Link': '%s/%s.git' %(GIST_URL,r.json()['id']),
			'Embed-Script': '<script src="%s/%s/%s.js"</script>' %(GIST_URL,self.username,r.json()['id']),
			'id': r.json()['id'],
			'created_at': r.json()['created_at'],

			}
			return response
		raise Exception('Gist not created: server response was [%s] %s' % (r.status_code, r.text))

