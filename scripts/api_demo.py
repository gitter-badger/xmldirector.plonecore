
import sys
import requests                     
from requests.auth import HTTPBasicAuth


base_url = 'http://localhost:12020/Plone/root'
username = 'admin'
password = 'admin'
auth = HTTPBasicAuth(username, password)
headers = {
    'accept': 'application/json',
    'content-type': 'application/json'
}


create_url = base_url + '/xmldirector-create'
result = requests.put(create_url, auth=auth, headers=headers)
if result.status_code != 201:
    print 'CREATE failed'
    sys.exit(1)
data_json = result.json()
print data_json


endpoint_url = data_json['url']
post_url = endpoint_url + '/xmldirector-store'
print post_url
files = {
    'sample.docx': ('sample.docx', open('test.docx', 'rb'), 'application/octet-stream'),
    'api_demo.py': ('api_demo.py', open('api_demo.py', 'rb'), 'application/octet-stream')
}
result = requests.post(post_url, auth=auth, files=files, headers=headers)
print result
if result.status_code != 200:
    print 'STORE failed'
    sys.exit(1)


listfull_url = endpoint_url + '/xmldirector-list-full'
result = requests.get(listfull_url, auth=auth, files=files, headers=headers)
if result.status_code != 200:
    print 'LIST FULL failed'
    sys.exit(1)
print result.json()
