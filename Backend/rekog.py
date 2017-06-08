import boto3
from urllib.request import urlopen
from orm import *
import csv

client = boto3.client('rekognition')

def get_accepted_tags():
	tags = dict()
	with open('tags.txt', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			tags[row[0]] = True
	return tags

def process_tags(uid, accepted_tags, url_tuple):
	url = url_tuple[0].replace('https://', 'http://')
	img_res = urlopen(url)
	img_bytes = img_res.read()

	if len(img_bytes) >= 5242880:
		print("Skipping too large file " + url)
		return

	aws_res = client.detect_labels(
			Image = {
				'Bytes': img_bytes
			},
			MinConfidence = 45
		)

	pic = Picture.create(uid=uid,url=url)
	pic.save()
	pid = pic.pid

	for label in aws_res['Labels']:
		name = label['Name']
		percent = int(label['Confidence'])

		if (not name in accepted_tags):
			continue

		tag = Tag.create(tag_text=name, percent=percent)
		tag.save()

		pictag = PicTags.create(pid=pid, tid=tag.tid)
		pictag.save()