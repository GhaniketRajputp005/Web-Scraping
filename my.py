import requests
url = "https://www.geu.ac.in/"
r= requests.get(url)
print(r.status_code)
print(r.text)