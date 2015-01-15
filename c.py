import time
from bs4 import BeautifulSoup
from mechanize import Browser
from re import search
import wget
from os import system,remove,path
import threading
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import urllib2
class somefunction(threading.Thread):
	def __init__(self,alpha):
		threading.Thread.__init__(self)
		self.alpha=alpha
	def run(self):
		try:
			ua="""Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36
			"""
			browser=Browser()
			browser.addheaders = [('User-Agent', ua), ('Accept', '*/*')]
			browser.set_handle_robots(False)
			print"===== Opening Browser===="
			browser.open("""https://images.google.com""")
			browser.select_form(nr=0)
			browser.form["q"]=self.alpha
			self.alpha=self.alpha.replace(".","")
			self.alpha=self.alpha.replace("(","")
			self.alpha=self.alpha.replace(")","")
			self.alpha=self.alpha.replace("'","")
			self.alpha=self.alpha.replace(" ","_")
			self.alpha=self.alpha.replace("&","")
			self.alpha=self.alpha.replace("*","")
			
			response=browser.submit()
			print "==== Ret Results ===";
			soup = BeautifulSoup(browser.response().read())
			body_tag = soup.body
	
			for a in soup.find_all('a', href=True):
				m1=search(r"imgurl=(.+\.png)",str(a['href']))
				m2=search(r"imgurl=(.+\.jpg)",str(a['href']))
				if m1:
					print "===downloading image==="
					filename=wget.download(m1.group(1))
					ext=".png"
					print "====Downloading done==="
					break
			
				if m2:
					print "===downloading image==="
					filename=wget.download(m2.group(1))
					ext=".jpg"
					print "====Downloading done==="	
					break
			pola='php 1.php "'+filename+'"  "'+self.alpha+'"'
			print pola
			system(pola)
			global images;
			images.append(self.alpha+ext)
			#remove(filename)
		except:
			pass

def upload_img(im):
	global client
	ext=path.splitext(im)[1]
	if ext==".png" or ext==".PNG":
		filename = im
		data = {
			'name': im,
			'type': 'image/png',  # mimetype
		}
		with open(filename, 'rb') as img:
        		data['bits'] = xmlrpc_client.Binary(img.read())
        	print "===========Uploading Image==========="
        	response = client.call(media.UploadFile(data))
        	print "===========Uploading DONE==========="
        	attachment_id = response['id']
        	relate(attachment_id)
        elif ext==".JPG" or ext==".jpeg" or ext==".jpg":
        	filename = im
		data = {
			'name': im,
			'type': 'image/jpeg',  # mimetype
		}
		with open(filename, 'rb') as img:
        		data['bits'] = xmlrpc_client.Binary(img.read())
        	print "===========Uploading Image==========="	
        	response = client.call(media.UploadFile(data))
        	print "===========Uploading Done==========="
        	attachment_id = response['id']
        	relate(attachment_id)
        else:
        	print "Cannot Upload .. Didn't Get Image Properly"
def relate(pid):
	sku=int(raw_input("Enter SKU   "))
	x="http://www.lifelineforyou.com/bcd/?sku="+str(sku)+"&pid="+str(pid)
	print x
	urllib2.urlopen(x).read()
	print "==========File Relation SUCCESS=============="
	

f=open('temp.csv','r')
threads=[]
images=[]
count=0
client =Client('http://lifelineforyou.com/xxx.php','resham','admin')
for line in f:
	#t=somefunction(line.strip())
	#t.start()
	#threads.append(t)
	if not line.strip()=="":
		t=somefunction(line.strip())
		t.start()
		threads.append(t)
	
	
for t in threads:
	t.join()
for im in images:
	print "Upload Image "+im+"   Y/N"
	agree=raw_input()
	if agree=='y' or agree=='Y':
		upload_img(im)
	else:
		pass

