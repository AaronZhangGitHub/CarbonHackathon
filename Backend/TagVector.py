import numpy as np
import os
from orm import *
import csv

class GenerateUserVector:
	def getVector(self, uid):
		print("Get vector called ")
		v = MyVector(uid)
		print("Vector initialized")
		v.createVectorTags()
		print("Vector tags created")
		v.createVectorTagOccurenceList()
		print("Vector to be returned")
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
		print("vector tag occurence lst being created")
		for tag in self._tagVector:
			print(tag)
			tagSum = self.getTagSum(tag)
			print("tag sum retrieved")
			tagIndex = self._tagVector.index(tag)
			print("tag index created")
			self._tagOccurenceVector.insert(tagIndex, tagSum)

	def getTagSum(self, tag_text):
		tagSum = 0
		print(tag_text)
		query = Tag.select().join(PicTags).join(Picture).where(Tag.tag_text == tag_text).where(Picture.uid == self._uid)
		print(query)
		for tag in query:
			print("retrieving from db")
			tagSum += tag.percent
		print("sum")
		return tagSum
