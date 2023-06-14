import requests
import os

#import from commandline / environment variables
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
SECRET_TOKEN = os.getenv('REDDIT_SECRET_TOKEN')
USERNAME = os.getenv('REDDIT_USERNAME')
PASSWORD = os.getenv('REDDIT_PASSWORD')

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

# res = requests.get("https://oauth.reddit.com/r/python/hot",
#                    headers=headers)

res = requests.get("https://oauth.reddit.com/r/tippytaps/hot", headers=headers)

print(res.json())  # let's see what we get
