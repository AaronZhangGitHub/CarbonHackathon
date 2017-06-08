import numpy as np
import os
from orm import *

class GenerateUserVector:
	def getVector(self, uid):
		v = Vector(uid)
		v.createVectorTags()
		v.createVectorTagOccurenceList()
		print(v.getTagList())
		print(v.getTagOccurenceVector())
		return v

class Vector:
	_tagVector = None #List of Tag namers
	_tagOccurenceVector = [] #List of Tag Percentage Sums
	_uid = None
	def __init__(self, userID):
		self._uid = userID
	def getTagList(self):
		#returns list of tags
		return self._tagVector
	def getTagOccurenceVector(self):
		#Returns list of tag percentage sums
		return self._tagOccurenceVector
	def createVectorTags(self):
		script_dir = os.path.dirname(__file__) 
		rel_path = "tags.txt"
		abs_file_path = os.path.join(script_dir, rel_path)
		with open(abs_file_path) as f:
			self._tagVector = list(f)
		with open(abs_file_path) as f:
			self._tagVector = [line.rstrip('\n') for line in f]
	def createVectorTagOccurenceList(self):
		for tag in self._tagVector:
			tagSum = self.getTagSum(tag, self._uid)
			tagIndex = self._tagVector.index(tag)
			self._tagOccurenceVector.insert(tagIndex, tagSum)
	def getTagSum(self, tag, uid):
		tagSum = 0
		for tag in Tag.select().join(PicTags).join(Picture).where(Picture.uid == uid).where(Tag.tag_text == tag):
			tagSum += tag.percent
		return tagSum