import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r= requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text,"lxml")

print(soup.find("p",{"class":"description"}).text)
print(soup.find("p",class_="description").string)

print(soup.find("h4",{"class":"pull-right price"}).string)
print(soup.find("h4",class_="pull-right price").string)

