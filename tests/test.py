from src.model import ClusteringModel
from test_data.test_data1 import test_data1

data = test_data1

model = ClusteringModel(data=data, num_of_clusters=3)
#clusters = model.spectral_clustering()
clusters, labels = model.mixed_clustering()
model.plot_clusters()

