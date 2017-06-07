import boto3
from urllib.request import urlopen
from orm import *

client = boto3.client('rekognition')

def load_labels(url):
	img_res = urlopen(url)
	img_bytes = img_res.read()

	if len(img_bytes) >= 5242880:
		print("Skipping too large file " + url)
		return

	aws_res = client.detect_labels(
			Image = {
				'Bytes': img_bytes
			},
			MinConfidence = 55
		)

	# Load the next index (check for existing)
	next_idx = 0
	try:
		next_idx = Tag.select(fn.Max(Tag.tag_index)).scalar() + 1
	except:
		pass

	tags = []
	for label in aws_res['Labels']:
		existing_tags = Tag.select().where(Tag.tag_text == label['Name']).limit(1)
		if len(existing_tags) == 0:
			existing_tag = Tag.create(tag_text=label['Name'], percent=int(label['Confidence']), tag_index=next_idx)
			existing_tag.save()
			next_idx += 1
		else:
			existing_tag = existing_tags[0]

		tags.append(existing_tag)

	return tags

