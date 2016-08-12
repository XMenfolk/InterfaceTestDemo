import httplib


http_client = None

http_client = httplib.HTTPConnection('192.168.217.130', 8080, timeout=30)
http_client.request('GET', '/jenkins/api/json?pretty=true')

response = http_client.getresponse()
print response.status
print response.read()