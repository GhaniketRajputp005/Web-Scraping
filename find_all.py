import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r= requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text,"lxml")

price =  soup.find_all("h4",class_ = "pull-right price")
# print(price.string) --> it'll not work on list of elements
# print(len(price))
# for i in price:
#     print(i.text)
# print(price[7])
desc = soup.find_all("p",class_ = "description")
# print(desc)
for i in desc:
    print(i.text)
