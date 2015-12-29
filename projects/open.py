import urllib
import urllib2

url=urllib2.urlopen('http://python.org/')
page=url.read()

print page
