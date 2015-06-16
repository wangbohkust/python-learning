from urllib import urlopen
#resource
import re


# Copy all of the content from the provided web page
webpage = urlopen('http://www.newthinktank.com/2014/04/').read()

# Grab everything that lies between the <title> by REGEX
patFinderTitle = re.compile('<title>(.*)</title>')
# Grab the link by a REGEX
patFinderLink = re.compile('<link rel.*href="(.*)" />')

# Store all of the titles and links found in webpage
findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)

listIterator=[]
listIterator[:] = range(2,5)
print findPatTitle
for i in listIterator:
   print i
   print findPatLink[i] 



