import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import SpectralClustering

from src.functions import calculate_weight_matrix, calculate_adjacency_matrix


class ClusteringModel:
    """
    Class of the clustering model
    """

    def __init__(self, data: dict, num_of_clusters: int = 0,
                 d_0: float = 1000.0, alpha_0: float = 50.0, g_0: float = 200.0):

        """
        :param data: dict : Raw data used for plotting
        :param num_of_clusters: int : Number of clusters we are looking for only used in the spectral clustering
        :param d_0: Real value added by the user to tune the working of the algorithm.
        :param alpha_0: Real value added by the user to tune the working of the algorithm.
        :param g_0: Real value added by the user to tune the working of the algorithm.
        """
        self.data = data
        self.num_of_clusters = num_of_clusters
        self.g_0 = g_0
        self.alpha_0 = alpha_0
        self.d_0 = d_0
        self.weight_matrix = calculate_weight_matrix(data=data, d_0=d_0, g_0=g_0, alpha_0=alpha_0)
        self.adjacency_matrix = calculate_adjacency_matrix(weight_matrix=self.weight_matrix)

    def clustering_with_threshold(self):
        """
        Calculates the clusters in the adjacency matrix
        :return: Dictionary of the sections with cluster's color
        """
        clusters = []

        #  Creates the list of the clusters based on the adjacency matrix

        for i in range(len(self.adjacency_matrix)):
            indices_list = list(np.nonzero(self.adjacency_matrix[i])[0])
            if len(indices_list) == 0:
                clusters.append([i])
            else:

                similarity_list = []
                for j in range(len(indices_list)):
                    similarity_list.append(indices_list[j])
                similarity_list.append(i)

                if sorted(similarity_list) not in clusters:
                    clusters.append(sorted(similarity_list))

        #  Merges the clusters with common elements

        for cluster in clusters:

            for other_cluster in clusters:

                if other_cluster != cluster:

                    if any(item in cluster for item in other_cluster):
                        new_cluster = cluster + other_cluster
                        clusters.append(new_cluster)

                        if other_cluster in clusters:
                            clusters.remove(other_cluster)
                        if cluster in clusters:
                            clusters.remove(cluster)

        #  Removes the duplicate indices from the clusters
        clusters_final = []

        for cluster in clusters:
            clusters_final.append(list(set(cluster)))

        #  Plotting the clusters with different colors

        color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        clusters_dict = {}
        i = 0
        c = 0
        for cluster in clusters_final:
            for index in cluster:
                clusters_dict[i] = {'color': color_list[c],
                                    'endpoint_1': self.data[list(self.data.keys())[index]]['endpoint_1'],
                                    'endpoint_2': self.data[list(self.data.keys())[index]]['endpoint_2']}
                i += 1
            c += 1

        for key in list(clusters_dict.keys()):
            plt.plot([clusters_dict[key]['endpoint_1'][0], clusters_dict[key]['endpoint_2'][0]],
                     [clusters_dict[key]['endpoint_1'][1], clusters_dict[key]['endpoint_2'][1]],
                     c=clusters_dict[key]['color'])
        plt.legend(['cluster 1', 'cluster 2', 'cluster 3'])
        plt.show()

        return clusters_dict

    def spectral_clustering(self):
        """
        Algorithm for the spectral clustering of the weight matrix.
        :return: list of the clusters where each the indices are the same as in the raw data
        """

        model = SpectralClustering(n_clusters=self.num_of_clusters)

        clusters_list = model.fit_predict(self.weight_matrix)

        #  Plotting the clusters

        color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        clusters_dict = {}
        i = 0

        for j in range(len(clusters_list)):
            clusters_dict[i] = {'color': color_list[clusters_list[j]],
                                'endpoint_1': self.data[list(self.data.keys())[j]]['endpoint_1'],
                                'endpoint_2': self.data[list(self.data.keys())[j]]['endpoint_2']}
            i += 1

        for key in list(clusters_dict.keys()):
            plt.plot([clusters_dict[key]['endpoint_1'][0], clusters_dict[key]['endpoint_2'][0]],
                     [clusters_dict[key]['endpoint_1'][1], clusters_dict[key]['endpoint_2'][1]],
                     c=clusters_dict[key]['color'])
        plt.show()
        return clusters_dict