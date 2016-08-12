from __future__ import print_function
import requests
from requests.auth import HTTPBasicAuth

url = 'http://192.168.217.130:8080/jenkins/job/check_python_version/disable'
request = requests.post(url, data={}, auth=('admin', 'admin'))

print(request.status_code)
print(request.headers)
print(request.reason)