import urllib2

request = urllib2.Request("https://github.com/RonakKhandelwal")

handle = urllib2.urlopen(request)

content = handle.read()

splitted_page = content.split("<span class=\"contrib-number\">")

splitted_page = splitted_page[1].split("</span>")

print "Contributions\t" + splitted_page[0]

