import requests
import json

from config import USERNAME, API_TOKEN

from mygist import Mygist
from do import Do
from comments import Comments

BASE_URL = 'https://api.github.com'

class Gist:
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
			'url': '%s/%s/%s' %(BASE_URL,self.username,r.json()['id']),
			'id': r.json()['id'],
			'created_at': r.json()['created_at'],

			}
			return response
		raise Exception('Gist not created.')


g = Gist()
#a = g.create(content='testing123')
#print a
#g.create(description='hello', public=1, name='test', content='test')
print g.profile().listall()
#print g.profile().list(13)
#print g.profile().content(name='bootstrap-min.css')
#print g.profile().content(id='5992283')
#print g.profile().starred(limit=1)
#print g.profile().starred()
#print g.profile().edit(description='bootstrap',name='bootstrap-min.css',content='header{color:white}')
#print g.profile().delete(id=a['id'])

#print g.do().star(id='5948959') #name='bootstrap-min.css' if authenticated

#print g.do().unstar(id='5948962')  

#print g.do().fork(id='3444905')

#print g.do().checkifstar(id='5948962')
#print g.search('geojeff').list(2)
#print g.profile().list(1)

#print g.search('geojeff').content(name='bt.py')

#print g.comments().listall(user='geojeff',name='bt.py')  #test wrong cases
#print g.comments().listall(name='bootstrap-min.css')

#print g.comments().create(id='5948962', body='hello')
#print g.comments().create(user='caspyin',name='curl.md', body='very helpful')

#print g.comments().delete(name='bootstrap-min.css', commentid='862454')
#print g.comments().get(name='bootstrap-min.css', commentid='862438')

#print g.comments().edit(name='bootstrap-min.css', commentid='862438',body='heya! world')