import feedparser
import time
import deskled

url = "https://www.ozbargain.com.au/feed"

class RssList:
        def __init__(self):
                self.lastentries = []
                self.entries = []

x = RssList()

def notify():
        print("flash flash")
        deskled.pwm()
        time.sleep(2)
        deskled.flasher(5,3) #how many, pause in seconds

def update_current():
        feed = feedparser.parse(url)
        for post in feed.entries:
                x.entries.extend(post.title)

def update_last():
        # feed = feedparser.parse( url )
        x.lastentries = x.entries
        # for post in feed.entries:
        #     lastentries.extend( post.title )

def check_diff():
        feed = feedparser.parse(url)
        if set(x.entries) ^ set(x.lastentries) == set([]):
                # print(entries)
                # print(lastentries)
                print("Sames")
        else:
                print("different")
                print(feed.entries[0].title)
                print(x.entries[0])
                update_last()
                print(x.lastentries[0])
                notify()

while True:
        x.entries = []
        update_current()
        # print(entries)
        # print(lastentries)
        check_diff()
        time.sleep(300)
