import numpy as np
import os
from orm import *
import csv

class GenerateUserVector:
	def getVector(self, uid):
		v = MyVector(uid)
		v.createVectorTags()
		v.createVectorTagOccurenceList()
		return v

class MyVector:
	def __init__(self, userID):
		self._uid = int(userID)
		self._tagVector = None
		self._tagOccurenceVector = []

	def getTagList(self):
		#returns list of tags
		return self._tagVector

	def getTagOccurenceVector(self):
		#Returns list of tag percentage sums
		return self._tagOccurenceVector

	def createVectorTags(self):
		self._tagVector = []
		with open('tags.txt', 'r') as file:
			reader = csv.reader(file)
			for row in reader:
				self._tagVector.append(row[0])

	def createVectorTagOccurenceList(self):
		for tag in self._tagVector:
			tagSum = self.getTagSum(tag)
			tagIndex = self._tagVector.index(tag)
			self._tagOccurenceVector.insert(tagIndex, tagSum)

	def getTagSum(self, tag_text):
		tagSum = 0
		for tag in Tag.select().join(PicTags).join(Picture).where(Tag.tag_text == tag_text).where(Picture.uid == self._uid):
			tagSum += tag.percent
		return tagSum
