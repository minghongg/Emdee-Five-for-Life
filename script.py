import requests
from bs4 import BeautifulSoup
import hashlib

url = 'http://docker.hackthebox.eu:31195/'

session = requests.Session()
response = session.get(url)

soup = BeautifulSoup(response.text,'html.parser')
#print(soup)

#get md5 value
value = soup.find_all('h3')[0].text
print(value)

#encode string to md5
md5 = hashlib.md5(value.encode()).hexdigest()

#send post request
payload = {'hash':md5}
data = session.post(url=url,data=payload)
print(data.text)