from src.functions import calculate_weight_matrix
from test_data.test_data1 import test_data1

data = test_data1
weight_matrix = calculate_weight_matrix(data=data, alpha_0=20.0, g_0=20.0, d_0=20.0)

print(weight_matrix)
