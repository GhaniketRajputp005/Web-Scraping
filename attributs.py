import requests
from bs4 import BeautifulSoup
url ="https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
# tag =  soup.header
# atb  =  tag.attrs
# print(atb)
# tag =  soup.header.div.a.button.span
tag  =  soup.div.ul.li.p
print(tag.string)