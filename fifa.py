#!/usr/bin/python
# -*- coding: utf-8 -*-


import requests
import json

headers = {#"Host": "signin.ea.com"
		   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:55.0) Gecko/20100101 Firefox/55.0"
		  , "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
		  , "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
		  , "Accept-Encoding": "gzip, deflate, br"
		  , "Content-Type": "application/x-www-form-urlencoded"
		  #, "Content-Length": 171
		  , "Referer": "https://signin.ea.com/p/web2/login?execution=e764183405s1&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fclient_id%3Dcustomer_portal%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fmyaccount.ea.com%252Fcp-ui%252Faboutme%252Flogin%26locale%3Den_US"
		  #, "Cookie": "JSESSIONID=C5CA68F980853DBE3F3A90A26A4484D7.prdaccountc-05; 
		  # utag_main=v_id:015eac55aaa10093e3922c7e0d5001052014100f0093c$_sn:4$_ss:1$_st:1506140838913$_pn:1%3Bexp-session$ses_id:1506139038913%3Bexp-session; 
		  # __utma=82955028.141173427.1506129851.1506137185.1506139041.6; __utmc=82955028; 
		  # __utmz=82955028.1506139041.6.5.utmcsr=easports.com|utmccn=(referral)|utmcmd=referral|utmcct=/"
		  , "Connection": "keep-alive"
		  , "Upgrade-Insecure-Requests": "1"
		  }
data = {"email": 123
		  , "password": 123
		  , "country": "US"
		  , "phoneNumber": ""
		  , "passwordForPhone": ""	
		  , "_rememberMe": "on"
		  , "rememberMe": "on"
		  , "_eventId": "submit"
		  , "gCaptchaResponse": ""
		  , "isPhoneNumberLogin": "false"
		  , "isIncompletePhone": ""}
url = 'https://signin.ea.com/p/web2/login?execution=e764183405s1&initref=https://accounts.ea.com:443/connect/auth?client_id=customer_portal&response_type=code&redirect_uri=https%3A%2F%2Fmyaccount.ea.com%2Fcp-ui%2Faboutme%2Flogin&locale=en_US'

r = requests.post(url = url, headers = headers, data = json.dumps(data))
# print type(r)
print r.history[0].body	
print r.status_code
# print r.encoding
print r.text
print type(r.cookies)




headers = {
			"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:55.0) Gecko/20100101 Firefox/55.0"
			, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
			, "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3"
			, "Accept-Encoding": "gzip, deflate, br"
			, "Cookie": "DOT_COM_PHPSESSID=lm7iptu5rv7ooi5tl18vnbh7m7; utag_main=v_id:015eac4e88b3001f891ad77af8d501052001900f0093c$_sn:2$_ss:0$_st:1506139127191$_pn:7%3Bexp-session$ses_id:1506135789725%3Bexp-session; ea2f4177=0; EASSSO=a0086fb4429ad6e5f36263d8a68b37407f314de7226316e8a6133907a8b3a27e; optimizelyEndUserId=oeu1506129383492r0.3149773621430576; optimizelySegments=%7B%22172174479%22%3A%22none%22%2C%22172202804%22%3A%22direct%22%2C%22172207507%22%3A%22false%22%2C%22172316047%22%3A%22ff%22%2C%22265568016%22%3A%22true%22%7D; optimizelyBuckets=%7B%7D; _ga=GA1.2.2041694134.1506129385; _gid=GA1.2.305525301.1506129385"
			, "Connection": "keep-alive"
			, "Upgrade-Insecure-Requests": "1"}
url = 'https://www.easports.com/'

print r.headers