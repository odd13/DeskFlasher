import time
from DeskLight import DeskLight
from RssFeed import RssFeed

desklight1 = DeskLight()
feed1 = RssFeed("https://www.ozbargain.com.au/feed")

while True:
	if (feed1.has_it_changed() == True):
		desklight1.flash(2,3)
		print(feed1.current_title)
		print(feed1.previous_title)	
		desklight1.dim_up_and_down()
		desklight1.turn_off()
	else:
		print("No Change")
		time.sleep(300)
