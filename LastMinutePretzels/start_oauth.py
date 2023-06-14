import sys
import requests
import os
import json

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

print("DEBUG AUTH RESPONSE: " + str(res), file=sys.stderr)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

print("DEBUG STARTING API CALL: ", file=sys.stderr)
# res = requests.get("https://oauth.reddit.com/r/tippytaps/hot", headers=headers)
res = requests.get("https://oauth.reddit.com/user/pretzels1337/saved", headers=headers)
        # note: it seems you can only get saved for your own user 

print(json.dumps(res.json()))  # let's see what we get
print("DEBUG FINISHED API CALL: ", file=sys.stderr)

#TODO PARSE OUT ALL THUMBNAILS

#STARTING WITH A COMMANDLINE EXAMPLE
# data > children [] { data > "thumbnail"
# parse on the commandline with jq 
# cat savedoutput.json | jq -r '.data.children[].data.thumbnail' | xargs -I foo curl --output-dir bar foo 
# download image
# curl 'https://b.thumbs.redditmedia.com/54hHDYVQ5-PpFmVz4jqaJgIx89tQyPiSVeIC0r3he-A.jpg' -out bar.jpg



