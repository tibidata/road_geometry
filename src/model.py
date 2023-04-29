import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from sklearn.cluster import SpectralClustering

from src.functions import calculate_weight_matrix, calculate_adjacency_matrix, create_clusters_dict


class ClusteringModel:
    """
    Class of the clustering model
    """

    def __init__(self, data: list, num_of_clusters: int = None,
                 d_0: float = 1000.0, alpha_0: float = 50.0, g_0: float = 200.0):

        """
        :param data: dict : Raw data used for plotting
        :param num_of_clusters: int : Number of clusters we are looking for only used in the spectral clustering
        :param d_0: Real value added by the user to tune the working of the algorithm.
        :param alpha_0: Real value added by the user to tune the working of the algorithm.
        :param g_0: Real value added by the user to tune the working of the algorithm.
        """
        self.labels = None
        self.clusters_dict = None
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

        graph = csr_matrix(self.adjacency_matrix)
        n_components, labels = connected_components(csgraph=graph)
        self.labels = labels

        print(n_components)

        #  Plotting the clusters with different colors

        color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        self.clusters_dict = create_clusters_dict(labels=list(self.labels), data=self.data)

        self.labels = labels

        return self.clusters_dict, self.labels, n_components

    def spectral_clustering(self):
        """
        Algorithm for the spectral clustering of the weight matrix.
        :return: list of the clusters where each the indices are the same as in the raw data
        """

        model = SpectralClustering(n_clusters=self.num_of_clusters, affinity='precomputed')

        self.labels = model.fit_predict(self.weight_matrix)

        self.clusters_dict = create_clusters_dict(data=self.data, labels=self.labels)

        return self.clusters_dict, self.labels

    def mixed_clustering(self):
        """
        Determining the number of clusters by using the threshold clustering, and using that as a parameter for
        spectral clustering.
        :return: clusters_dict, labels of clusters
        """
        clusters_dict, labels, self.num_of_clusters = self.clustering_with_threshold()

        self.clusters_dict, self.labels = self.spectral_clustering()

        return self.clusters_dict, self.labels

    def plot_clusters(self):
        """
        Method to plot the predicted clusters. Raises exception if none of the models were ran before.
        :return: None
        """

        if self.labels is None or self.clusters_dict is None:
            raise Exception('Please run the model first to plot the results.')
        else:
            print('plotting')
            for key in list(self.clusters_dict.keys()):
                print(key)
                plt.plot([self.clusters_dict[key]['endpoint_1'][0], self.clusters_dict[key]['endpoint_2'][0]],
                         [self.clusters_dict[key]['endpoint_1'][1], self.clusters_dict[key]['endpoint_2'][1]],
                         c=self.clusters_dict[key]['color'])

            plt.show()
