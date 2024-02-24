import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ticker.finology.in/"
r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_="table table-sm table-hover screenertable")
# print(table.text)

header = table.find_all("th")
# print(header)
titles = []
for i in header:
    title = i.text
    titles.append(title)
# print(titles)

df = pd.DataFrame(columns=titles)
# df.to_csv("myfile.csv")
# df.to_excel("my.xlsx")

# print(df)
rows = table.find_all("tr")
# print(rows)
for i in rows[1:]:
    # print(i.text)
    data = i.find_all("td")
    row = [j.text.strip() for j in data]
    # print(row)
    l = len(df)
  #  df.loc[l] = row
print(df)

df.to_excel("my.xlsx")

# list comprehension in python
# what is strip method in python
