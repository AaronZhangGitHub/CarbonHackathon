from orm import *
from TagVector import *
import numpy as np

def random():
	vg = GenerateUserVector()
	vs = []
	for uid in uids:
		v = vg.getVector(uid).getTagOccurenceVector()
		vs.append(v)
	uids = [ user.uid for user in [ IGUsers.get_by_handle(handle) for handle in handles ]]

class AggregatedVectorStatistics:
	def __init__(self, uidList):
		self._uidList = uidList
		self._tagOccurenceVectorList = []
		self._sumOfTagsList = []
		self._tagMeanValueList = []
	def createVectorValues(self):
		guv = GenerateUserVector()
		print("Get Here")
		for uid in self._uidList:
			print(uid)
			tempOccurenceVector = guv.getVector(uid).getTagOccurenceVector()
			print("Get here")
			self._tagOccurenceVectorList.append(tempOccurenceVector)
			print("Get here")
	def getV(self):
		return self._tagOccurenceVectorList
	def sumTags(self):
		self._sumOfTagsList = [0]*len(self._tagOccurenceVectorList[0])
		for tov in self._tagOccurenceVectorList:
			for i in range(len(tov)):
				self._sumOfTagsList[i]+= tov[i]
		print(self._sumOfTagsList)
	def computeMeanValues(self):
		for i in range(len(self._sumOfTagsList)):
			self._tagMeanValueList.append(self._sumOfTagsList[i]/self.getNumberOfUsers())
		print(self._tagMeanValueList)
	def getMeanValueTagList(self):
		return self._tagMeanValueList
	def getSumValueTagList(self):
		return self._sumOfTagsList
	def getNumberOfUsers(self):
		return len(self._tagOccurenceVectorList)
	def writeToFileTagOccurenceVector(self):
		open('tagstatinfo.txt', 'w').close()
		fileToWrite = open('TagOccurenceVectorList.txt', 'w')
		for vector in self._tagOccurenceVectorList:
			fileToWrite.write("%s\n" % vector)
	def writeToFileMeanValues(self):
		open('tagstatinfo.txt', 'w').close()
		fileToWrite = open('TagOccurenceVectorList.txt', 'w')
		for vector in self._tagOccurenceVectorList:
			fileToWrite.write("%s\n" % vector)

uids = [ user.uid for user in IGUsers.select() ]
print(uids)
avs = AggregatedVectorStatistics(uids)
print(avs.getV())
print("a")
avs.createVectorValues()
print("b")
avs.writeToFile()
#print(len(avs.getV()))
#avs.sumTags()
#avs.computeMeanValues()
#a = avs.getMeanValueTagList()
#b = avs.getSumValueTagList()
#print(a)
#print(b)