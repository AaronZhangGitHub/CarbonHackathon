from TagVector import *
from sklearn import svm
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn import manifold
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

uid = 3
userVectorGen = GenerateUserVector()
userVector = userVectorGen.getVector(uid)
print(userVector.getTagOccurenceVector())
print(userVector.getTagList())
x = np.matrix([ [1, 4, 9], [5, 6, 7], [ -1, 5, 10 ] ]).reshape(3,-1)

def plot(x):
	z = cosine_similarity(x)

	normInvert = np.vectorize(lambda (x): 1-x)
	z = normInvert(z)

	mds = manifold.MDS(n_components=3, max_iter=3000, eps=1e-9, dissimilarity="precomputed")
	pos = mds.fit(z).embedding_
	clf = PCA(n_components=3)
	pos - clf.fit_transform(pos)

	fig = plt.figure(1)
	ax = Axes3D(fig)

	ax.scatter(pos[:,0], pos[:,1], pos[:,2], s=100)

	plt.show()