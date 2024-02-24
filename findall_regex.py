import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Quantum_computing"
r= requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text,"lxml")

# data =  soup.find_all(["h4","a","p"])
# data =  soup.find_all(string =  "Galaxy Note")  --> to get data using string
data = soup.find_all(string = re.compile("quantum computing"))
print(len(data))
