import feedparser
import time
import deskled

url = "https://www.ozbargain.com.au/feed"
lastentries = []
entries = []

def notify():
  deskled.pwm()
  time.sleep(2)
  deskled.flasher(5,3) #how many, pause in seconds

def update_current():
  feed = feedparser.parse( url )
  for post in feed.entries:
        entries.extend( post.title )
	
def update_last():
  #feed = feedparser.parse( url )
  lastentries = entries
  #for post in feed.entries:
  #	lastentries.extend( post.title )

def check_diff():
  feed = feedparser.parse( url )
  if set(entries) ^ set(lastentries) == set([]):
	#print(entries)
	#print(lastentries)
        print("Sames")

  else:
        print("different")
	print(feed.entries[0].title)
	update_last()
	notify()


while True:
  entries = []
  update_current()
  #print(entries)
  #print(lastentries)
  check_diff()  
  time.sleep(300)



