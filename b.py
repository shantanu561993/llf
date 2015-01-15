from bs4 import BeautifulSoup
from mechanize import Browser
from re import search
ua="""Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36
"""
f=open('a.html','r')
data=f.read().replace('\n', '')
soup = BeautifulSoup(data)
body_tag = soup.body
all_links = soup.find_all('a')
for a in all_links:
	m1=search(r"imgurl=(.+\.png)",str(a))
	m2=search(r"imgurl=(.+\.jpg)",str(a))
	if m1:
		print m1.group(1)
	if m2:
		print m2.group(1)
