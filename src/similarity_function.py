import math
import numpy as np


def similarity(d_0: float, alpha_0: float,
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

    """Length of the i section."""

    l_i = math.dist(i_end1, i_end2)

    """Length of the j section."""

    l_j = math.dist(j_end1, j_end2)

    """Midpoints of the i and j sections."""

    mid_i = np.array((i_end1[0] + i_end2[0]) / 2, (i_end1[1] + i_end2[1]) / 2)
    mid_j = np.array((j_end1[0] + j_end2[0]) / 2, (j_end1[1] + j_end2[1]) / 2)

    """Length of the section created with the midpoints."""

    d_ij = math.dist(mid_i, mid_j)

    """The smallest between the endpoints."""

    g_ij = min(math.dist(i_end1, j_end1), math.dist(i_end1, j_end2), math.dist(i_end2, j_end1),
               math.dist(i_end2, j_end2))

    """Vectors created from the sections i, j and the midpoints."""

    vect_i = i_end1 - i_end2
    vect_j = j_end1 - j_end2
    vect_m = mid_i - mid_j

    """The angle between section i and midpoints section."""

    alpha_i = math.degrees(math.acos(np.dot(vect_i, vect_m) /
                                     (np.sqrt(vect_i.dot(vect_i)) * np.sqrt(vect_m.dot(vect_m)))))

    """The angle between section j and the midpoints section."""

    alpha_j = math.degrees(math.acos(np.dot(vect_j, vect_m) /
                                     (np.sqrt(vect_j.dot(vect_j)) * np.sqrt(vect_m.dot(vect_m)))))

    """
    Defining the 3 parts of the equation.
    """

    first_part = (abs(((l_i + l_j) / 2) - d_ij) ** 2) / d_0

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
    The weight ha its maximum iff the two sections have a mutual end point, are on the same line and have a connection.
    """

    return weight
