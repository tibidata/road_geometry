import numpy as np
from src.functions import calculate_weight_matrix, calculate_adjacency_matrix
from test_data.test_data1 import test_data1

"""Code snippet to test the optimal values for tuning the algorithm"""

sample_adjacency_matrix = np.array([[0, 1, 1, 0, 0, 0, 0],
                                    [1, 0, 1, 0, 0, 0, 0],
                                    [1, 1, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 1, 0, 0],
                                    [0, 0, 0, 1, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0, 0, 0]])

test_values = [0.1, 0.5, 1, 5, 10, 20, 30, 50, 100, 200, 1000]

difference_dict = {}
j = 0
for alpha in range(len(test_values)):

    for d in range(len(test_values)):
        for g in range(len(test_values)):
            weight_matrix = calculate_weight_matrix(d_0=test_values[d], alpha_0=test_values[alpha], g_0=test_values[g],
                                                    data=test_data1)
            adjacency_matrix = calculate_adjacency_matrix(weight_matrix)
            sum_difference = 0
            for i in range(len(adjacency_matrix)):
                difference = np.linalg.norm(adjacency_matrix[i] - sample_adjacency_matrix[i])
                sum_difference = sum_difference + difference
            difference_dict[str(j)] = {'g0': test_values[g], 'alpha0': test_values[alpha], 'd0': test_values[d],
                                       'difference': sum_difference}
            j = j + 1
            if sum_difference <= 4:
                print('d0 =', test_values[d], ' ,g0=', test_values[g], ' ,alpha0=', test_values[alpha])
                print('difference = ', sum_difference)
                print(adjacency_matrix)

sorted_dict = sorted(difference_dict.items(), key=lambda x: x[1]['difference'])
