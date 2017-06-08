import numpy as np
import os
#tagVector1 = np.array([99, 72, 41, 98])
#tagVector2 = np.array([31, 44, 41, 99])

def main():
	v = Vector()
	#v.computeVector()
	#print(v.getVector())
	print(len(v.createVectorTags()))

class Vector:
	_userVector = None
	_tagVector = None
	#Each vector represents a user
	def getVector(self):
		return 
	def computeVector(self):
		self._userVector = np.array([99, 72, 41, 98])
	def getVector(self):
		return self._userVector
	def createVectorTags(self):
		script_dir = os.path.dirname(__file__) 
		rel_path = "tags.txt"
		abs_file_path = os.path.join(script_dir, rel_path)
		with open(abs_file_path) as f:
			self._tagVector = list(f)
		with open(abs_file_path) as f:
			self._tagVector = [line.rstrip('\n') for line in f]
		return self._tagVector
main()