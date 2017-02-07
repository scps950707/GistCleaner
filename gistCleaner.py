#!/usr/bin/env python
import sys
import requests
import json
from requests.auth import HTTPBasicAuth
if len(sys.argv) != 3:
    print('Usage:./gistCleaner.py [username] [password]')
    sys.exit()
user = sys.argv[1]
passwd = sys.argv[2]
gistsJsonResponse = requests.get('https://api.github.com/users/' + user + '/gists', auth=HTTPBasicAuth(user, passwd))
if gistsJsonResponse.status_code == 200:
    contents = json.loads(gistsJsonResponse.content)
    if len(contents) == 0:
        print('No gists in github')
    else:
        for content in contents:
            print('delete:' + content['id'])
            requests.delete('https://api.github.com/gists/' + content['id'], auth=HTTPBasicAuth(user, passwd))
        print(str(len(contents)) + ' gists cleaned')
else:
    print('username or password incorrect')
