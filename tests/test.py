from src.functions import calculate_weight_matrix, calculate_adjacency_matrix, clustering_with_threshold, \
    spectral_clustering
from test_data.test_data1 import test_data1

data = test_data1
weight_matrix = calculate_weight_matrix(data=data, alpha_0=50.0, g_0=200, d_0=1000)

adjacency = calculate_adjacency_matrix(weight_matrix=weight_matrix)

clusters = clustering_with_threshold(adjacency_matrix=adjacency, data=data)


print(clusters)
