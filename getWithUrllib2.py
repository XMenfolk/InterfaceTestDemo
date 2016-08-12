import urllib2

response = urllib2.urlopen('http://192.168.217.130:8080/jenkins/api/json?pretty=true')
print response.read()