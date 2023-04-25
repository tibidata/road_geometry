from test_data.test_data1 import test_data1
from src.model import ClusteringModel
import numpy as np

data = test_data1

model = ClusteringModel(data=data, num_of_clusters=3)
clusters = model.clustering_with_threshold()


