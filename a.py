import time
from bs4 import BeautifulSoup
from mechanize import Browser
from re import search
import wget
from os import system,remove
import thread
def somefunction(alpha):
	ua="""Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36
	"""
	browser=Browser()
	browser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]
	browser.set_handle_robots(False)
	print"===== Opening Browser===="
	browser.open("""https://images.google.com""")
	browser.select_form(nr=0)
	browser.form["q"]=alpha
	alpha=alpha.replace(".","")
	alpha=alpha.replace("(","")
	alpha=alpha.replace(")","")
	alpha=alpha.replace("'","")
	alpha=alpha.replace(" ","_")
	response=browser.submit()
	print "==== Ret Results ===";
	soup = BeautifulSoup(browser.response().read())
	body_tag = soup.body
	all_links = soup.find_all('a')
	count=0
	for a in all_links:
		m1=search(r"imgurl=(.+\.png)",str(a))
		m2=search(r"imgurl=(.+\.jpg)",str(a))
		if m1:
			print "===downloading image==="
			filename=wget.download(m1.group(1))
			print "====Downloading done==="
			break
		if m2:
			print "===downloading image==="
			filename=wget.download(m2.group(1))
			print "====Downloading done==="
			break
	system("php 1.php "+filename+" "+alpha)
	remove(filename)


f=open('temp.csv','r')
for line in f:
	thread.start_new_thread(somefunction,(line,))
while True:
	pass

