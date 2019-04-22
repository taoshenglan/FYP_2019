# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

linkset = set()
txtName = "data3.txt"
contentName = 'cat3.txt'
f=open(txtName, "a+",encoding='UTF-8')
f2=open(contentName, "a+",encoding='UTF-8')
# to get the content of the website
def content(siteName):
	site = 'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/'
	sh= requests.get(site + siteName + '/monthly/2018010100/2018013100','lxml')
	context = sh.text + '\n\n'
	f2.write(context)

def solvepage(all_url):
	title = []
	tmp_href = []
	start_html = requests.get(all_url, headers=headers)

	soup = BeautifulSoup(start_html.text, 'lxml')
	#get heading of the parent site
	all_title = soup.find('h1', id='firstHeading')
	head = all_title.get_text()
	#get heading of children sites
	all_a = soup.find('div', class_='mw-category-generated')
	if all_a is None:
		return []

	page = all_a.find(id='mw-pages')
	if page is not None:
		name = page.find_all('a')
		for n in name:

			f2.write('Title: ' + head + '\n')
			content(n.get_text())
			new_context = head + '\t' + n.get_text()+ '\n'
			f.write(new_context)
	sub = all_a.find(id='mw-subcategories')
	if sub is not None:
		heds = sub.find_all('li')
		link = []
		for h in heds:
			a = h.find('a')
			link.append(a)
		for a in link:
			if a not in linkset:
				f2.write('Title: ' + a.get_text() + '\n')
				content(a.get_text())
				new_context = head + '\t' + a.get_text() + '\n'
				f.write(new_context)
				tmp_href.append(a['href'])
				linkset.add(a)
		for li in tmp_href:
			tmp = solvepage("https://en.wikipedia.org{}".format(li))




if __name__ == "__main__":

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
							 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
	all_url = 'https://en.wikipedia.org/wiki/Category:Anime'
	solvepage(all_url)
	f.close()
	f2.close()
