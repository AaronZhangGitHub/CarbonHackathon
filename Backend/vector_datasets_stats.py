from orm import *
from TagVector import *
import numpy as np


class AggregatedVectorStatistics:
	def __init__(self, uidList):
		self._uidList = uidList
		self._tagOccurenceVectorList = []
		self._sumOfTagsList = []
		self._tagMeanValueList = []
	def createVectorValues(self):
		guv = GenerateUserVector()
		for uid in self._uidList:
			tempOccurenceVector = guv.getVector(uid).getTagOccurenceVector()
			self._tagOccurenceVectorList.append(tempOccurenceVector)
	def getV(self):
		return self._tagOccurenceVectorList
	def sumTags(self):
		self._sumOfTagsList = [0]*len(self._tagOccurenceVectorList[0])
		for tov in self._tagOccurenceVectorList:
			for i in range(len(tov)):
				self._sumOfTagsList[i]+= tov[i]
	def computeMeanValues(self):
		for i in range(len(self._sumOfTagsList)):
			self._tagMeanValueList.append(self._sumOfTagsList[i]/self.getNumberOfUsers())
	def getMeanValueTagList(self):
		return self._tagMeanValueList
	def getSumValueTagList(self):
		return self._sumOfTagsList
	def getNumberOfUsers(self):
		return len(self._tagOccurenceVectorList)
	def writeToFileTagOccurenceVector(self):
		open('TagOccurenceVectorList.txt', 'w').close()
		with open('TagOccurenceVectorList.txt', 'w') as fileToWrite:
			for vector in self._tagOccurenceVectorList:
				fileToWrite.write("%s\n" % vector)
			fileToWrite.close()
	def writeToFileMeanValues(self):
		print("writing to mean values")
		open('meanvalues.txt', 'w').close()
		with open('meanvalues.txt', 'w') as fileToWrite:
			for vector in self._tagMeanValueList:
				print(vector)
				fileToWrite.write("%s\n" % vector)
	def writeToFileSumValues(self):
		open('sumvalues.txt', 'w').close()
		with open('sumvalues.txt', 'w') as fileToWrite:
			for vector in self._sumOfTagsList:
				print(vector)
				fileToWrite.write("%s\n" % vector)

def main():
	uids = [ user.uid for user in IGUsers.select() ]
	print(uids)
	avs = AggregatedVectorStatistics(uids)
	print(avs.getV())
	print("a")
	avs.createVectorValues()
	print("b")
	avs.sumTags()
	avs.computeMeanValues()
	avs.writeToFileTagOccurenceVector()
	avs.writeToFileMeanValues()
	avs.writeToFileSumValues()
try:
	before_request_handler()
	main()
finally:
	after_request_handler()
#print(len(avs.getV()))
#avs.sumTags()
#avs.computeMeanValues()
#a = avs.getMeanValueTagList()
#b = avs.getSumValueTagList()
#print(a)
#print(b)