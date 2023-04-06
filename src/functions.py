import math
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(formatter={'float': lambda x: "{0:0.5f}".format(x)})


def calculate_similarity(d_0: float, alpha_0: float,
                         g_0: float, i_end1: np.array, i_end2: np.array, j_end1: np.array,
                         j_end2: np.array):
    """
    The function to compare the 2 sections i and j.
    :param i_end1: First end point of section i.
    :param i_end2: Second endpoint of section i.
    :param j_end1: First end point of section j.
    :param j_end2: Second endpoint of section j.
    :param d_0: Real value chosen by the user
    :param alpha_0: Real value chosen by the user
    :param g_0: Real value chosen by the user
    :return: weight := similarity value between 0 and 1
    """

    """Midpoints of the i and j sections."""

    mid_i = np.array(((i_end1[0] + i_end2[0]) / 2, (i_end1[1] + i_end2[1]) / 2))
    mid_j = np.array(((j_end1[0] + j_end2[0]) / 2, (j_end1[1] + j_end2[1]) / 2))

    """Length of the section created with the midpoints."""

    d_ij = math.dist(mid_i, mid_j)

    """The smallest between the endpoints."""

    g_ij = min(math.dist(i_end1, j_end1), math.dist(i_end1, j_end2), math.dist(i_end2, j_end1),
               math.dist(i_end2, j_end2))

    """Vectors created from the sections i, j and the midpoints."""

    vect_i = i_end1 - i_end2
    vect_j = j_end1 - j_end2
    vect_m = mid_i - mid_j

    if d_ij != 0:

        """The angle between section i and midpoints section."""

        alpha_i = math.degrees(math.acos(np.dot(vect_i, vect_m) /
                                         (np.sqrt(vect_i.dot(vect_i)) * np.sqrt(vect_m.dot(vect_m)))))
        """Handling the cases when the angle is clock-wise"""
        if alpha_i > 90:
            alpha_i = 180 - alpha_i

        """The angle between section j and the midpoints section."""

        alpha_j = math.degrees(math.acos(np.dot(vect_j, vect_m) /
                                         (np.sqrt(vect_j.dot(vect_j)) * np.sqrt(vect_m.dot(vect_m)))))

        """Handling the cases when the angle is clock-wise"""

        if alpha_j > 90:
            alpha_j = 180 - alpha_j

        """
        Defining the 3 parts of the equation.
        """

        first_part = d_ij ** 2 / d_0

        """
        Distance of the midpoints of i and j 0 iff the midpoints are the same.
        """

        second_part = (2 - math.cos(2 * alpha_i) - math.cos(2 * alpha_j)) / alpha_0

        """
        0 iff the i and j sections are on the same line.
        """

        third_part = g_ij / g_0

        """
        0 iff the i and j sections has a mutual endpoint.
        """

        weight = math.exp(-first_part - second_part - third_part)

        """
        The weight has its maximum iff the two sections have a mutual end point,
        are on the same line and have a connection.
        """
    else:
        weight = 0

    return weight


def calculate_weight_matrix(data: dict, d_0: float, alpha_0: float, g_0: float):
    """
    Calculates the W weight matrix using the similarity function.
    :param data: Dictionary of the data
    :param d_0: Real value added by the user to tune the working of the algorithm.
    :param alpha_0: Real value added by the user to tune the working of the algorithm.
    :param g_0: Real value added by the user to tune the working of the algorithm.
    :return:  W weight matrix.
    """

    sections = list(data.keys())

    W = np.zeros((len(sections), len(sections)))

    for i in range(len(sections)):
        for j in range(len(sections)):
            i1 = np.array(data[sections[i]]['endpoint_1'])
            i2 = np.array(data[sections[i]]['endpoint_2'])
            j1 = np.array(data[sections[j]]['endpoint_1'])
            j2 = np.array(data[sections[j]]['endpoint_2'])
            W[i, j] = calculate_similarity(d_0=d_0, alpha_0=alpha_0, g_0=g_0, i_end1=i1,
                                           i_end2=i2, j_end1=j1, j_end2=j2)

    return W


def calculate_adjacency_matrix(weight_matrix: np.array):
    """Adjacency matrix of the weights"""

    adjacency_matrix = np.zeros_like(weight_matrix)

    """Non-zero elements of the weight matrix"""
    n = sum(list(np.count_nonzero(weight_matrix, axis=1)))

    """Average of the weight matrix"""
    average = np.sum(weight_matrix) / n

    """Variance of the weight matrix"""
    variance = 0
    for i in range(len(weight_matrix)):
        for j in range(len(weight_matrix)):
            x = (average - weight_matrix[i, j]) ** 2
            variance = variance + x

    variance = variance / n

    """Entropy of the weight matrix"""
    entropy = 0

    for i in range(len(weight_matrix)):
        for j in range(len(weight_matrix)):
            if weight_matrix[i, j] != 0:
                x = weight_matrix[i, j] * math.log2(weight_matrix[i, j])
                entropy = entropy + x
            else:
                entropy = entropy

    entropy = (-1 / n) * entropy

    """Threshold of the clustering"""
    threshold = average + variance - entropy

    for i in range(len(weight_matrix)):
        for j in range(len(weight_matrix)):
            if weight_matrix[i, j] < threshold:
                adjacency_matrix[i, j] = 0
            else:
                adjacency_matrix[i, j] = 1

    return adjacency_matrix


def clustering_with_threshold(adjacency_matrix: np.array, data: dict):
    """
    Calculates the clusters in the adjacency matrix
    :param data: Used for plotting the clusters
    :param adjacency_matrix: NxN matrix where N is the number of the sections
    :return: Dictionary of the sections with cluster's color
    """
    clusters = []

    """Creates the list of the clusters based on the adjacency matrix"""

    for i in range(len(adjacency_matrix)):
        indices_list = list(np.nonzero(adjacency_matrix[i])[0])
        if len(indices_list) == 0:
            clusters.append([i])
        else:

            similarity_list = []
            for j in range(len(indices_list)):
                similarity_list.append(indices_list[j])
            similarity_list.append(i)

            if sorted(similarity_list) not in clusters:
                clusters.append(sorted(similarity_list))

    """Merges the clusters with common elements"""

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

    """Removes the duplicate indices from the clusters"""
    clusters_final = []

    for cluster in clusters:
        clusters_final.append(list(set(cluster)))

    """Plotting the clusters with different colors"""

    color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    clusters_dict = {}
    i = 0
    c = 0
    for cluster in clusters_final:
        for index in cluster:
            clusters_dict[i] = {'color': color_list[c], 'endpoint_1': data[list(data.keys())[index]]['endpoint_1'],
                                'endpoint_2': data[list(data.keys())[index]]['endpoint_2']}
            i = i + 1
        c = c + 1

    for key in list(clusters_dict.keys()):
        plt.plot([clusters_dict[key]['endpoint_1'][0],clusters_dict[key]['endpoint_2'][0]],
                 [clusters_dict[key]['endpoint_1'][1],clusters_dict[key]['endpoint_2'][1]], c=clusters_dict[key]['color'])
    plt.legend(['cluster 1', 'cluster 2', 'cluster 3'])
    plt.show()

    return clusters_dict


def spectral_clustering(weight_matrix: np.array, num_clusters: int):
    """Diagonal matrix where the D_ij = the sum of the elements of the ith row of the weight matrix"""
    D = np.zeros_like(weight_matrix)
    for i in range(len(weight_matrix)):
        D[i, i] = sum(weight_matrix[i])

    """Obtained from the equation X = D^(-1/2) W D^(-1/2)"""

    D_inv_sqrt = np.sqrt(np.linalg.inv(D))

    X = np.dot(D_inv_sqrt, weight_matrix).dot(D_inv_sqrt)

    eigen_values, eigen_vectors = np.linalg.eig(X)

    return eigen_values, eigen_vectors
