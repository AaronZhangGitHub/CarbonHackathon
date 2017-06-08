import httplib2
import urllib
import json 
import sys

def scrape_location_data(username, img_code):
	h = httplib2.Http()
	resp, content = h.request("http://www.instagram.com/p/%s/?taken-by=%s" % (img_code, username))
	beg_index = content.find(b"window._sharedData = ")
	end_index = content.find(b";</script>")
	trimmed_content = content[beg_index:end_index]
	trimmed_content = trimmed_content.replace(b"window._sharedData = ",b"")

	insta_array = json.loads(trimmed_content, encoding='utf-8')
	media = insta_array['entry_data']['PostPage'][0]['graphql']['shortcode_media']['location']
	if media:
		return str(media['name'])
	else:
		return None

def scrape_insta(username, count=20):
	h = httplib2.Http()
	resp, content = h.request("http://instagram.com/%s" % username)
	beg_index = content.find(b"window._sharedData = ")
	end_index = content.find(b";</script>")
	trimmed_content = content[beg_index:end_index]
	trimmed_content = trimmed_content.replace(b"window._sharedData = ",b"")

	insta_array = json.loads(trimmed_content, encoding='utf-8')
	
	# Iterate over all of the user's photos
	img_array = []
	i = 0
	while len(img_array) < count:
		media = insta_array['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]

		if media['is_video']: # Don't include videos
			pass
		else:
			location = scrape_location_data(username, media['code'])
			img_array.append((str(media['display_src']), location))
		i += 1

	return img_array