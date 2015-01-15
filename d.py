import threading
import time
import wget
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
    	
    	wget.download("http://www.tutorialspoint.com/python/python_multithreading.htm");
        #print "Starting " + self.name
        print "";
        #print "Exiting " + self.name

f=open('aaa.txt','w')
for i in xrange(10000):
	myThread(i+1, "Thread"+str(i+1), i+1).start()
	f.write(str(threading.activeCount()))
