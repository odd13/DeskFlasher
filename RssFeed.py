import feedparser

class RssFeed:
	def __init__(self, url):
		self.current_title = ""
		self.previous_title = "" 
		self.feed = feedparser.parse(url)
		self.update_to_current_title()

	def update_feed(self):
		self.feed = feedparser.parse(self.feed.url)

	def update_to_current_title(self):
		self.update_feed()
		self.current_title = self.feed.entries[0].title 
  
	def has_it_changed(self):
		self.update_to_current_title()
		if (self.current_title == self.previous_title):
			return False
		else:
			self.previous_title = self.current_title
			return True
