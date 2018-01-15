#!/usr/bin/python
import requests,threading,time
from lxml import etree
from bs4 import BeautifulSoup
def getHtml(url):
	#url = 'http://www.doutula.com/article/list/?page=1'
	header = {'User-Agent':'Mozilla/4.0 (Macintosh; Intel Mac OS X 9_1_3) AppleWebKit/37.36 (KHTML, like Gecko) Chrome/1.0.3163.100 Safari/37.36'}
	request = requests.get(url=url,headers=header)
	response = request.content
	return response
def getImage_url(html):
	soup = BeautifulSoup(html,'lxml')
	all_a = soup.find_all('a',class_ = 'list-group-item')
	for i in all_a:
		img_html = getHtml(i['href'])
		get_img(img_html)
def get_img(html):
	soup = etree.HTML(html)
	items = soup.xpath('//div[@class = "artile_des"]')
	for items in items:
		imgurl_list = items.xpath('table/tbody/tr/td/a/img/@onerror')
		for i in imgurl_list:
			fin_url = i.split('=')[-1]
			#print type(fin_url)
			img_list = fin_url.replace("'","")
			print img_list
			img_content = requests.get(url=img_list)
			with open('/Carl/Desktop/picture/ %s'% img_list.split('/')[-1],'wb') as f:  #replace your own path
				f.write(img_content.content)
def main():
	print "[+]  " + "It's working ..."
	print "[+]  " + "Download the picture ..."
	time.sleep(3)
	url = 'http://www.doutula.com/article/list/?page={}'
	for i in range(1,10):
		htmlCon = getHtml(url.format(i))
		getImage_url(htmlCon)
if __name__ == '__main__':
	main()

#html= getHtml()
#getImage_url(html)
	
