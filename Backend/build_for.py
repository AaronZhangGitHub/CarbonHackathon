import rekog
import instagram_scraper
from orm import *
import sys

def build_for(handle):
	accepted_tags = rekog.get_accepted_tags()

	user = IGUsers.create(handle=handle)
	user.save()

	urls = instagram_scraper.scrape_insta(user.handle, 15)
	for url in urls:
		rekog.process_tags(user.uid, accepted_tags, url)

if len(sys.argv) > 0:
	build_for(sys.argv[1])
else:
	print("Missing handle!")