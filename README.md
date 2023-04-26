# Modeling Road Geometry With Spectral Clustering And Graph Theory

The algorithms are based on a thesis for the University Of Szeged written by Robert Fazekas. The basic idea was to use 
graph theory to model the road geometry.
More information about the underlying mathematics can be found in this 
interlinked [study](https://www.researchgate.net/publication/337456737_Clustering_Algorithm_Exploring_Road_Geometry_in_a_Video-Based_Driver_Assistant_System).

## Short description of the algorithms

<img src="https://lucid.app/publicSegments/view/798ed4dd-fdbf-4310-a9b0-ea1ffa01bdd5/image.png"/>


## Usage

The input of the model is a dictionary with as many key-value pairs as the number of
the sections we want to cluster. An example data set can be found in the 
test_data directory.

## src directory

The directory consists of two python files: functions and model.

The functions.py file is used by the model to calculate similarity, create matrices needed during the steps of the
algorithm.

The model.py file contains the model:
 - .clustering_with_threshold():
   - the implementation of the first algorithm
   - to use it first instantiate the model
   - to plot the predicted clusters use the .plot_clusters() method after predicting the clusters.

 - .spectral_clustering():
   - the implementation of the second algorithm
   - to use it first instantiate the model
   - to plot the predicted clusters use the .plot_clusters() method after predicting the clusters
 
 - .mixed_clustering():
   - calculates the number of expected clusters with the .clustering_with_threshold() method
   - then uses that number to use .spectral_clustering() method
 
 - .plot_clusters():
   - plots the predicted clusters
   - only can be used after running any of the clustering algorithms

## Requirements

The list of the necessary libraries can be found in the requirements.txt file.

## Additional informations

For a deeper understanding of the project and the underlying mathematics please check the project_plan.md markdown file.


