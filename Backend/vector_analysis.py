from TagVector import *
from sklearn import svm
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.decomposition import PCA
from sklearn import manifold
import numpy as np
from orm import IGUsers

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gen_plot(handles, colors):
	# Convert handles to user ids
	uids = [ user.uid for user in [ IGUsers.get_by_handle(handle) for handle in handles ]]

	# Get vectors for each user and convert to matrix
	vg = GenerateUserVector()
	vs = []
	for uid in uids:
		v = vg.getVector(uid).getTagOccurenceVector()
		vs.append(v)

	x = np.matrix(vs).reshape(len(uids),-1).astype(np.float64)
	pos = transform_matrix(x) # Plot based on cosine similarity
	plot(pos, colors)

def transform_matrix(x):
	z = euclidean_distances(x)

	# normInvert = np.vectorize(lambda x: 1-x)
	# z = normInvert(z)

	mds = manifold.MDS(n_components=3, metric=True, dissimilarity="precomputed")
	pos = mds.fit(z).embedding_

	clf = PCA(n_components=3)
	return clf.fit_transform(pos)

def plot(pos, colors):
	fig = plt.figure(1)
	ax = Axes3D(fig)
	ax.scatter(pos[:,0], pos[:,1], pos[:,2], s=100, c=colors)
	plt.show()

gen_plot([ 'greerglenn', 'therock', 'brandt.io', 'sdotcurry', 'kingjames' ],
		 [ 'red'       , 'blue'   , 'green'    , 'purple'   , 'orange'    ])