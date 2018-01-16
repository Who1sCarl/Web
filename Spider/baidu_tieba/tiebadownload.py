import re
import requests
import urllib
print "[+]please enter tieba's url:"
url=raw_input()
status=requests.session()
def getPage(status):
	text=status.get(url)
	html=text.text
	return html
page=getPage(status)
def getImage(html):
	reg = r'src=\\&quot;(.*?\.jpg)'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	finalist=[i.replace('\\','') for i in imglist]
	x=0
	for imgurl in finalist:
		urllib.urlretrieve(imgurl,'/Users/Carl/Desktop/%s.jpg' %x)
		x+=1
html = getPage(status)
getImage(html)
print "[+]downloads the pictures..."
print '[+]finished...'
print '[+]enjoy!'
 