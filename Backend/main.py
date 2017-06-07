import rekog
import instagram_scraper
from orm import *

def main():
	accepted_tags = rekog.get_accepted_tags()

	user = IGUsers.create(handle="greerglenn")
	user.save()

	urls = instagram_scraper.scrape_insta(user.handle)
	for url in urls:
		rekog.process_tags(user.uid, accepted_tags, url)

main()