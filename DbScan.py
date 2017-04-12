from sklearn.cluster import DBSCAN
from CsvImporter import Importer

import pandas as pd, numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from shapely.geometry import MultiPoint
from geopy.distance import great_circle

class DbScan:
    def test(self):
        importer = Importer()
        arr = importer.get_data("XXX")

        kms_per_radian = 6371.0088
        # define epsilon as 1.5 kilometers, converted to radians for use by haversine
        epsilonAsKm = 50
        epsilon = epsilonAsKm / kms_per_radian
        #to be a frequent location you should be there at least 10 % of your time
        minSamples = int(len(arr) * 0.05)
        print(minSamples)
        X = np.asarray(arr)

        db = DBSCAN(eps=epsilon, min_samples=minSamples,algorithm='ball_tree', metric='haversine').fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        print(labels)
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


        print('Estimated number of clusters: %d' % n_clusters_)

        clusters = pd.Series([X[labels==n] for n in range(n_clusters_)])


        def get_centermost_point(cluster):
            centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
            centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
            return tuple(centermost_point)

        def get_outermost_point(cluster):
            centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
            outermost_point = max(cluster, key=lambda point: great_circle(point, centroid).m)
            return tuple(outermost_point)


        centermost_points = clusters.map(get_centermost_point)
        outermost_point = clusters.map(get_outermost_point)
        print(centermost_points)
        print(outermost_point)
        import matplotlib.pyplot as plt

        # Black removed and is used for noise instead.
        unique_labels = set(labels)
        colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
        for k, col in zip(unique_labels, colors):
            if k == -1:
                # Black used for noise.
                col = 'k'

            class_member_mask = (labels == k)

            xy = X[class_member_mask & core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                    markeredgecolor='k', markersize=14)

            xy = X[class_member_mask & ~core_samples_mask]
            plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                    markeredgecolor='k', markersize=6)

        plt.title('Estimated number of clusters: %d' % n_clusters_)
        plt.show()


    def run(self, data):
        kms_per_radian = 6371.0088
        # define epsilon as 1.5 kilometers, converted to radians for use by haversine
        epsilonAsKm = 50
        epsilon = epsilonAsKm / kms_per_radian
        #to be a frequent location you should be there at least 10 % of your time
        minSamples = int(len(data) * 0.1)
        X = np.asarray(data)

        db = DBSCAN(eps=epsilon, min_samples=minSamples,algorithm='ball_tree', metric='haversine').fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        #print(labels)
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


        #print('Estimated number of clusters: %d' % n_clusters_)
        clusters = pd.Series([X[labels==n] for n in range(n_clusters_)])


        def get_centermost_point(cluster):
            centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
            centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
            return tuple(centermost_point)

        centermost_points = clusters.map(get_centermost_point)
        #return centermost_points
        return labels

    def run_and_prepare_data(self, data):
        #add one new feature to each feature vector for each common location
        _indexArr = []
        _validDataPoints = []
        #filter out invalid data and save the index of valid data in data
        for row, n in zip(data, range(len(data))):
            if (data[n][0] is not None and data[n][1] is not None):
                _indexArr.append(n)
                _validDataPoints.append(row)
        #run db scan get an array with -1 for noise, 0 for first cluster, 1 for second cluster ...
        labels = self.run(_validDataPoints)
        #get each unique value in labels (-1, 0, 1) for 2 clusters with nosie
        geoPointsFeatures = set(labels)
        
        #map our db scan result back to our data array and add a dimension for each cluster
        resultArr = []
        for n in range(len(data)):
            tmpArr = []
            if (n in _indexArr and labels[_indexArr.index(n)] == -1 or n not in _indexArr):
                tmpArr.append(1)
            else:
                tmpArr.append(0)
            
            for feature in geoPointsFeatures:
                if (feature == -1):
                    continue
                if (n in _indexArr and feature == labels[_indexArr.index(n)]):
                    tmpArr.append(1)
                else:
                    tmpArr.append(0)
            resultArr.append(tmpArr)
        return resultArr


#algo = DbScan()
#importer = Importer()
#arr = importer.get_data("marius-geodata.csv")
#print(len(algo.run(arr)))