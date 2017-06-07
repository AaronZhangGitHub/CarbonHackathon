import boto3
from urllib.request import urlopen
from orm import *

client = boto3.client('rekognition')

def load_labels(uid, url):
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

	pic = Picture.create(uid=uid)
	pic.save()
	pid = pic.pid

	for label in aws_res['Labels']:
		tag = Tag.create(tag_text=label['Name'], percent=int(label['Confidence']))
		tag.save()
		tid = tag.tid

		pictag = PicTags.create(pid=pid, tid=tid)
		pictag.save()