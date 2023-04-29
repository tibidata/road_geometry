from src.model import ClusteringModel
from test_data.test_data1 import test_data2

data = test_data2

model = ClusteringModel(data=data, num_of_clusters=2)

model.clustering_with_threshold()

model.plot_clusters()




