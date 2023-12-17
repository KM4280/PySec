import requests
from bs4 import BeautifulSoup as BS
from bs4 import Comment

URL = 'http://92.205.177.169:83/'
requ = requests.get(URL)

soup = BS(requ.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
flag = ""
for i in comments:
	lhs, rhs = i.split(":", 1)
	fl, lhs = rhs.split("#", 1)
	flag = flag + fl
flag = str(flag)
print(flag)


