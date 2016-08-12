import urllib2
import urllib

post_data = urllib.urlencode({})
response = urllib2.urlopen('http://192.168.217.130:8080/jenkins/job/check_python_version/build', post_data)

print response.read()
print response.getheaders()