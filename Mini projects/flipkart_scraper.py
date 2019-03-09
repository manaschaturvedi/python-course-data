import requests
from bs4 import BeautifulSoup


def flipkart(s):
	"""
	A web scraper that scraps the titles of products listed on the first page of Flipkart's
	search results based on a search keyword
	"""
	url = 'http://www.flipkart.com/search?q=' + str(s) + '&as=off&as-show=off&otracker=start'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, "html.parser")

	for link in soup.findAll('a', {'class' : '_2cLu-l'}):
		print(link.get('title'))
		print('-'*50)

flipkart('python')
