import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
print(r.status_code)
#print(soup.div) 
#print(r.text) --> gives html format of a website
print(soup.p)