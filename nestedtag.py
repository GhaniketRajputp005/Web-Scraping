import requests
from bs4 import BeautifulSoup
# url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
url ="https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
# boxes  = soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
# print(len(boxes))
# box = soup.find_all("div",class_ = "col-sm-4 col-lg-4 col-md-4")[8]
# # print(box)
# name =  box.find("a").text
# print(name)
# desc = box.find("p",class_ =  "description").text
# print(desc)
# review  =  box.find("p",class_ ="pull-right").string
# print(review)

navbar =  soup.find_all("ul",class_ ="nav",id = "side-menu")[0]
# print(navbar.text)
name =  soup.find("li",class_="active")
# print(name.text)
import requests
from bs4 import BeautifulSoup
# url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
url ="https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
# boxes  = soup.find_all("div",class_="col-sm-4 col-lg-4 col-md-4")
# print(len(boxes))
# box = soup.find_all("div",class_ = "col-sm-4 col-lg-4 col-md-4")[8]
# # print(box)
# name =  box.find("a").text
# print(name)
# desc = box.find("p",class_ =  "description").text
# print(desc)
# review  =  box.find("p",class_ ="pull-right").string
# print(review)

navbar =  soup.find_all("ul",class_ ="nav",id = "side-menu")[0]
print(navbar.text)
name =  navbar.find_all("li")[2]
print(name.text)
nav = name[2].find("ul",class_="nav nav-second-level collapse in")
print(nav.text)
# nav =  soup.find_all("ul",class_ ="nav nav-second-level collapse in")
# print(nav)
