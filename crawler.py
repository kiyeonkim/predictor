# -*- coding: utf-8 -*- 

import os
import sys
import requests
import json
from bs4 import BeautifulSoup

def getNewsList(keyword):
	print "Naver news Crawling Start..."
	print "NewsList crawling..."

	client_id = "jAkDRT1pDS9F29HCkz8Y"
	client_secret = "jqn06G68ny"

	api_url = 'https://openapi.naver.com/v1/search/news.json'
	headers = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
	payload = {'query':keyword}

	r = requests.get(api_url, headers=headers, params=payload)

	# print r.status_code
	# print r.headers['content-type']
	# print r.encoding
	# print r.text
	# print r.json()

	return r.json()

def getNews(url):
	r = requests.get(url)

	return r.text

def htmlParser(html_text):
	soup = BeautifulSoup(html_text, 'html.parser')
	# print soup.prettify()
	# print soup.find_all('p')

	return soup.find_all('p')

if __name__ == "__main__":
	# for each in getNews("애플")['items']:
	# 	print "========================="
	# 	print each['title']
	# 	print each['description']
	link = getNewsList("삼성전자")['items'][2]['originallink']

	print link

	for each in htmlParser(getNews(link)):
		print each