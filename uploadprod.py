import requests
import urllib 
f=open('temp.csv','r')
for line in f:
	c1,c2,c3,c4,pd,pr=line.strip().split(';');
	c1=urllib.pathname2url(c1.strip())
	c2=urllib.pathname2url(c2.strip())
	c3=urllib.pathname2url(c3.strip())
	c4=urllib.pathname2url(c4.strip())
	pd=urllib.pathname2url(pd.strip())
	pr=urllib.pathname2url(pr.strip().rstrip('/-'))
	#print pr
	payload={'cat1':c1,"cat2":c2,"cat3":c3,"cat4":c4,"prod":pd,"price":int(pr)}
	r=requests.post("http://URL/main/pricelist/temp.php",data=payload)
	print r.text
	
	

	
	
