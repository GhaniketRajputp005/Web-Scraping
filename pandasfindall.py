import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.text, "lxml")
names = soup.find_all("a", class_="title")
# print(names)
# print("PRODUCT NAME\n")
product_name = []
for i in names:
    product_name.append(i.text)

# print(product_name)

# print("\nPRODUCT PRICE\n")

prices = soup.find_all("h4", class_="pull-right price")
product_price = []
for i in prices:
    product_price.append(i.text)
# print(product_price)

# print("\nPRODUCT DESCRIPTION\n")


desc = soup.find_all("p", class_="description")
product_description = []
for i in desc:
    product_description.append(i.text)
# print(product_description)

# print("\nPRODUCT REVIEW\n")


rev = soup.find_all("p", class_="pull-right")
product_review = []
for i in rev:
    product_review.append(i.text)
# print(product_review)

df = pd.DataFrame({"Product Name": product_name, "Prices": product_price,
                  "Description": product_description, "Reviews": product_review})
# df.to_csv("product details.csv") can be converted to csv or excel file
df.to_excel("product file.xlsx")
