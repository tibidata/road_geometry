import itertools
import math

import numpy as np
import scipy


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

    # Midpoints of the i and j sections.

    mid_i = np.array(((i_end1[0] + i_end2[0]) / 2, (i_end1[1] + i_end2[1]) / 2))
    mid_j = np.array(((j_end1[0] + j_end2[0]) / 2, (j_end1[1] + j_end2[1]) / 2))

    # Length of the section created with the midpoints.

    d_ij = math.dist(mid_i, mid_j)

    # The smallest distance between the endpoints.

    g_ij = min(math.dist(i_end1, j_end1), math.dist(i_end1, j_end2), math.dist(i_end2, j_end1),
               math.dist(i_end2, j_end2))

    # Vectors created from the sections i, j and the midpoints.

    vect_i = i_end1 - i_end2
    vect_j = j_end1 - j_end2
    vect_m = mid_i - mid_j

    if d_ij != 0:

        # The angle between section i and midpoints section.

        alpha_i = math.degrees(math.acos(np.dot(vect_i, vect_m) /
                                         (np.sqrt(vect_i.dot(vect_i)) * np.sqrt(vect_m.dot(vect_m)))))
        # Handling the cases when the angle is clock-wise
        if alpha_i > 90:
            alpha_i = 180 - alpha_i

        # The angle between section j and the midpoints section.

        alpha_j = math.degrees(math.acos(np.dot(vect_j, vect_m) /
                                         (np.sqrt(vect_j.dot(vect_j)) * np.sqrt(vect_m.dot(vect_m)))))

        # Handling the cases when the angle is clock-wise

        if alpha_j > 90:
            alpha_j = 180 - alpha_j

        # Defining the 3 parts of the equation.

        midp_dist = d_ij ** 2 / d_0

        # Distance of the midpoints of i and j 0 iff the midpoints are the same.

        linearity = (2 - math.cos(2 * alpha_i) - math.cos(2 * alpha_j)) / alpha_0

        # 0 iff the i and j sections are on the same line.

        connection = g_ij / g_0

        # 0 iff the i and j sections has a mutual endpoint.

        weight = math.exp(-midp_dist - linearity - connection)

        #  The weight has its maximum iff the two sections have a mutual end point,
        #  are on the same line and have a connection.

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

    W = np.zeros((len(data), len(data)))

    i = 0  #  row index of the weight matrix
    j = 0  #  column index of the weight matrix

    x_prev = data[0]  #  first element of the data used for handling the row, column index changes

    for x, y in itertools.combinations(data, 2):

        #  During the for loop both i and j starts from 0. We are using itertools.combinations which gives the
        #  Combination of the elements of a list. [A,B,C] -> AB, AC, BC
        #  With this method we get un upper triangular matrix with the weights, we will have to transpose it after
        #  and add the 2 matrices together to get the weight matrix.

        if x_prev != x:
            #  When we finished comparing an element with the rest the row index increases.
            i += 1
            j = i + 1
        else:
            #  After comparing two elements the column index increases
            j += 1

        similarity = calculate_similarity(d_0=d_0, alpha_0=alpha_0, g_0=g_0,
                                          i_end1=np.array(x[0]), i_end2=np.array(x[1]),
                                          j_end1=np.array(y[0]), j_end2=np.array(y[1]))
        W[i, j] = similarity
        x_prev = x

    return W.T + W


def calculate_adjacency_matrix(weight_matrix: np.array):
    """
    :param weight_matrix: ndarray : Weight matrix calculated with the similarity function
    :return: ndarray : Adjacency matrix
    """

    #  Non-zero elements of the weight matrix
    n = sum(list(np.count_nonzero(weight_matrix, axis=1)))

    #  Average of the weight matrix
    average = np.mean(weight_matrix)

    #  Variance of the weight matrix
    variance = np.var(weight_matrix)

    #  Entropy of the weight matrix
    entropy = (-1 / n) * scipy.stats.entropy(weight_matrix)[0]

    #  Threshold of the clustering
    threshold = average + variance - entropy

    #  Comparing weights with threshold
    threshold_lambda = lambda x: 0 if x < threshold else 1
    threshold_vect = np.vectorize(threshold_lambda)

    adjacency_matrix = threshold_vect(weight_matrix)

    return adjacency_matrix


def create_clusters_dict(labels: list, data: list):
    """
    Function to create the cluster dictionary. Used for plotting
    :param labels: list : cluster of the elements
    :param data: dict : raw data
    :return:
    """
    color_list = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    clusters_dict = {}

    for i in range(len(labels)):
        clusters_dict[i] = {'color': color_list[labels[i]],
                            'endpoint_1': data[i][0],
                            'endpoint_2': data[i][1]}
        print(type(np.array(data[i][0])))

    return clusters_dict
