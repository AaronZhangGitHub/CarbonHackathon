from TagVector import *
from sklearn import svm
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.decomposition import PCA
from sklearn import manifold
import numpy as np
from orm import IGUsers
from sklearn.cluster import KMeans

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def gen_plot(handles, colors):
	# Convert handles to user ids
	
	uids = [ user.uid for user in [ IGUsers.get_by_handle(handle) for handle in handles ]]
	try:
		before_request_handler()
		if uid == None:
			return [ x for x in IGUsers.get_distinct_handles().dicts() ]
		else:
			return [ x for x in IGUsers.get_distinct_handles().where(IGUsers.uid == uid).limit(1).dicts() ]
	finally:
			after_request_handler()
	# Get vectors for each user and convert to matrix
	vg = GenerateUserVector()
	vs = []
	for uid in uids:
		v = vg.getVector(uid).getTagOccurenceVector()
		vs.append(v)

	x = np.matrix(vs).reshape(len(uids),-1).astype(np.float64)
	pos = transform_matrix(x) # Plot based on cosine similarity
	plot(pos, colors)
	cluster(pos, 4)
	plt.show()

def transform_matrix(x):
	z = euclidean_distances(x)

	# normInvert = np.vectorize(lambda x: 1-x)
	# z = normInvert(z)

	mds = manifold.MDS(n_components=3, metric=True, dissimilarity="precomputed")
	pos = mds.fit(z).embedding_

	clf = PCA(n_components=3)
	return clf.fit_transform(pos)

def cluster(pos, n_clusters):
	fig = plt.figure(2)
	ax = Axes3D(fig)
	clusterer = KMeans(n_clusters = n_clusters)
	clusterer.fit(pos)
	labels = clusterer.labels_
	ax.scatter(pos[:,0], pos[:,1], pos[:,2], s=100, c=labels, edgecolors='black')

def plot(pos, colors):
	fig = plt.figure(1)
	ax = Axes3D(fig)
	ax.scatter(pos[:,0], pos[:,1], pos[:,2], s=100, c=colors, edgecolors='black')

gen_plot([ 'greerglenn', 'therock', 'brandt.io', 'sdotcurry', 'kingjames', 'steveyeun', 'mikeescamilla', 'madonna'  , 'knapp_city', 'thejordanbranddotcom', 'yaser_cm', 'mostafanasr20' ],
		 [ 'red'       , 'blue'   , 'green'    , 'purple'   , 'orange'   , 'blue'     , 'black'        , 'turquoise', 'magenta'   , 'red'                 , 'yellow'  , 'white' ])