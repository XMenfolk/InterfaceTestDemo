import requests

request = requests.get('http://192.168.217.130:8080/jenkins/api/json?pretty=true')
print request.text