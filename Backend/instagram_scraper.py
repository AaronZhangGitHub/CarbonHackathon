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

def scrape_insta_page(username, max_id):
	# print("Loading %s at page %s" % (username, max_id))
	url = "http://instagram.com/%s" % username
	if max_id != None: url += "?max_id=%s" % str(max_id)

	h = httplib2.Http()
	resp, content = h.request(url)
	beg_index = content.find(b"window._sharedData = ")
	end_index = content.find(b";</script>")
	trimmed_content = content[beg_index:end_index]
	trimmed_content = trimmed_content.replace(b"window._sharedData = ",b"")

	insta_array = json.loads(trimmed_content, encoding='utf-8')
	return insta_array['entry_data']['ProfilePage'][0]['user']['media']['nodes']


def scrape_insta(username, count=10, max_id=None):
	profile = scrape_insta_page(username, max_id)

	found_ids = dict()
	
	# Iterate over all of the user's photos
	img_array = []
	i = 0
	offset = 0
	while len(img_array) < count:
		# If pase end of this profile, load next
		if i-offset >= len(profile):
			offset += len(profile)
			profile = scrape_insta_page(username, profile[-1]['id'])
		media = profile[i-offset]

		if media['is_video']: # Don't include videos
			pass
		else:
			found_ids[media['id']] = found_ids.get(media['id'], 0) + 1

			display_src = str(media['display_src'])
			location = scrape_location_data(username, media['code'])
			img_array.append((display_src, location))
		i += 1

	return img_array