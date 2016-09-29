import json
import requests
from config import BASE_URL, GIST_URL

class Mygist:
	def __init__(self, gist, **args):
		self.gist = gist
		if 'user' in args:
			self.user = args['user']
		else:
			self.user = self.gist.username

	def listall(self):
		'''
		will display all the filenames.
		Result can be stored in an array for easy fetching of gistNames
		for future purposes.
		eg. a = Gist().mygists().listall()
		    print a[0] #to fetch first gistName
		'''
		file_name = []
		r = requests.get(
			'%s/users/%s/gists' % (BASE_URL, self.user),
			headers=self.gist.header
			)
		r_text = json.loads(r.text)
		limit = len(r.json())
		if (r.status_code == 200 ):
			for g,no in zip(r_text, range(0,limit)):
				for key,value in r.json()[no]['files'].iteritems():
					file_name.append(value['filename'])
			return file_name

		raise Exception('Username not found')

	def list(self, offset):
		'''
		will display only the required no. of filenames but in order.
		Result can be stored in an array for easy fetching of gistNames
		for future purposes.
		eg. a = Gist().mygists().listall()
		    print a[0] #to fetch first gistName
		'''
		file_name = []
		r = requests.get(
			'%s/users/%s/gists' %(BASE_URL,self.user),
			headers=self.gist.header
			)
		if (r.status_code == 200 ):
			r_text = json.loads(r.text)
			limit = offset if (offset <= len(r.json()) ) else len(r.json())

			for g,no in zip(r_text, range(0,limit)):
				for key,value in r.json()[no]['files'].iteritems():
					file_name.append(value['filename'])
			return file_name
		raise Exception('Username not found')

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

	def content(self, **args):
		'''
		Doesn't require manual fetching of gistID of a gist
		passing gistName will return the content of gist. In case,
		names are ambigious, provide GistID or it will return the contents
		of recent ambigious gistname
		'''
		self.gist_name = ''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Either provide authenticated user\'s Unambigious Gistname or any unique Gistid')


		if self.gist_id:
			r = requests.get(
				'%s'%BASE_URL+'/gists/%s' %self.gist_id,
				headers=self.gist.header
				)
			if (r.status_code == 200):
				r_text = json.loads(r.text)
				if self.gist_name!='':
					content =  r.json()['files'][self.gist_name]['content']
				else:
					for key,value in r.json()['files'].iteritems():
						content = r.json()['files'][value['filename']]['content']
				return content

		raise Exception('No such gist found')

	def getgist(self, **args):

		if 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Gist ID must be provided')

		if self.gist_id:
			r = requests.get(
				'%s/gists/%s'%(BASE_URL,self.gist_id),
				headers=self.gist.header,
				)
			if (r.status_code == 200):

				for key,value in r.json()['files'].iteritems():
						content = value['filename']
				return content

		raise Exception('No such gist found')


	def edit(self, **args):
		'''
		Doesn't require manual fetching of gistID of a gist
		passing gistName will return edit the gist
		'''
		self.gist_name = ''
		if 'description' in args:
			self.description = args['description']
		else:
			self.description = ''


		if 'name' in args and 'id' in args:
			self.gist_name = args['name']
			self.gist_id = args['id']
		elif 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Gist Name/ID must be provided')

		if 'content' in args:
			self.content = args['content']
		else:
			raise Exception('Gist content can\'t be empty')

		if (self.gist_name == ''):
			self.gist_name = self.getgist(id=self.gist_id)
			data = {"description": self.description,
  				"files": {
    				self.gist_name: {
      				"content": self.content
    				}
  				}
  		}
		else:
			data = {"description": self.description,
  				"files": {
    				self.gist_name: {
      				"content": self.content
    				}
  				}
  			}


		if self.gist_id:
			r = requests.patch(
				'%s/gists/%s'%(BASE_URL,self.gist_id),
				headers=self.gist.header,
				data=json.dumps(data),
				)
			if (r.status_code == 200):
				r_text = json.loads(r.text)
				response = {
					'updated_content': self.content,
					'created_at': r.json()['created_at'],
					'comments':r.json()['comments']
				}

				return response

		raise Exception('No such gist found')


	def delete(self, **args):
		'''
		Delete a gist by gistname/gistID
		'''

		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Provide GistName to delete')

		url = 'gists'
		if self.gist_id:
			r = requests.delete(
				'%s/%s/%s'%(BASE_URL,url,self.gist_id),
				headers=self.gist.header
				)
			if (r.status_code == 204):
				response = {
					'id': self.gist_id,
				}
				return response

		raise Exception('Can not delete gist')


	def starred(self, **args):
		'''
		List the authenticated user's starred gists
		'''
		ids =[]
		r = requests.get(
			'%s/gists/starred'%BASE_URL,
			headers=self.gist.header
			)

		if 'limit' in args:
			limit = args['limit']
		else:
			limit = len(r.json())

		if (r.status_code == 200):
			for g in range(0,limit ):
				ids.append('%s/%s/%s' %(GIST_URL,r.json()[g]['user']['login'],r.json()[g]['id']))
			return ids

		raise Exception('Username not found')

	def links(self,**args):
		'''
		Return Gist URL-Link, Clone-Link and Script-Link to embed
		'''
		if 'name' in args:
			self.gist_name = args['name']
			self.gist_id = self.getMyID(self.gist_name)
		elif 'id' in args:
			self.gist_id = args['id']
		else:
			raise Exception('Gist Name/ID must be provided')
		if self.gist_id:
			r = requests.get(
				'%s/gists/%s'%(BASE_URL,self.gist_id),
				headers=self.gist.header,
				)
			if (r.status_code == 200):

				content = {
				'Github-User': r.json()['user']['login'],
				'GistID': r.json()['id'],
				'Gist-Link': '%s/%s/%s' %(GIST_URL,self.gist.username,r.json()['id']),
				'Clone-Link': '%s/%s.git' %(GIST_URL,r.json()['id']),
				'Embed-Script': '<script src="%s/%s/%s.js"</script>' %(GIST_URL,self.gist.username,r.json()['id'])
				}
				return content

		raise Exception('No such gist found')