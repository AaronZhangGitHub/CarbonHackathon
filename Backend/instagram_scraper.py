# from time import sleep
# from instagram.client import InstagramAPI

# access_token = "1187105088.1677ed0.92d6d724ed3b46d1a8982ab4c1cdb899"
# client_secret = "b99326b73cbb45ce9b97e7af82434cf6"

# api = InstagramAPI(access_token=access_token, client_secret=client_secret)
# recent_media, next = api.user_recent_media(user_id="userid", count=10)
# for media in recent_media:
#    print media.caption.text

import httplib2
import urllib
import json 
import sys

def scrape_insta(username):
	h = httplib2.Http()
	resp, content = h.request("http://instagram.com/%s" % username)
	beg_index = content.find("window._sharedData = ")
	end_index = content.find(";</script>")
	trimmed_content = content[beg_index:end_index]
	trimmed_content = trimmed_content.replace("window._sharedData = ", "")

	insta_array = json.loads(trimmed_content, encoding='utf-8')
	
	# Iterate over all of the user's photos
	img_array = []
	i = 0
	while len(img_array) < 10:
		media = insta_array['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]

		if media['is_video']: # Don't include videos
			pass
		else:
			img_array.append(str(media['display_src']))
		i += 1

	return img_array
	
