'''
	Either configure here or use command line arguments
	-U/--username for username eg. -U 'softvar' or --username 'softvar'
	_p/--password for password eg. -P 'secret_password' or --password 'secret_password'
'''
# Your Github username
USERNAME = ''

# Your Github API TOKEN
API_TOKEN = ''
# By default setting Limit to fetch no of gists of authenticated user
# or use -L/--limit as command-line arguments
# Github API will always return <= 30 recent gists.
LIMIT = None

BASE_URL = 'https://api.github.com'
GIST_URL = 'https://gist.github.com'