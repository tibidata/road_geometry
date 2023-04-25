# Project plan

## Table of contents

1) Short description of the project
2) Description of the used technologies
3) Short description of the algorithms
4) Image processing
5) Testing the algorithms
6) Milestones
7) MVP

## Short description of the project

> The project is a school project for the 'Computer aided modeling' course at the University of Szeged. The goal of the
> project is to implement two clustering algorithms based on a paper published by Judit Nagy-György, Norbert Bogya,
> Zsolt
> Vizi and Róbert Fazekas. The algorithms are already implemented in Matlab my goal is to implement them in python.

## Description of the used technologies

> During the project I'm planning to use several python libraries:
> - Imageio
> - Matplotlib
> - Numpy
> - OpenCV
> - Pandas
> - Scipy
> - Skimage
> - Sklearn

> Development environment:
> - PyCharm

> Version control system:
> - Github

> If needed I will use other programming languages like Go or Julia.

## Short description of the algorithms

<!--suppress ALL -->
<img src="https://lucid.app/publicSegments/view/798ed4dd-fdbf-4310-a9b0-ea1ffa01bdd5/image.png"/>

## Studies and papers

> 1) [Clustering Algorithm Exploring Road Geometry in a Video-Based Driver Assistant System](https://www.researchgate.net/publication/337456737_Clustering_Algorithm_Exploring_Road_Geometry_in_a_Video-Based_Driver_Assistant_System)
> 2) [Image Segmentation using Python’s scikit-image module](https://www.geeksforgeeks.org/image-segmentation-using-pythons-scikit-image-module/)
> 3) [Grouping Line-segments using Eigenclustering](https://www.researchgate.net/publication/216360795_Grouping_Line-segments_using_Eigenclustering)
> 4) [Scikit image documentation](https://scikit-image.org/docs/stable/index.html#)
> 5) [Imageio documentation](https://imageio.readthedocs.io/en/stable/)

## Image processing

> Since the image processing algorithm mentioned in the original paper is an industrial secret I am going to use
>
an [image segmentation algorithm](https://www.geeksforgeeks.org/image-segmentation-using-pythons-scikit-image-module/) (
> Segmentation by Thresholding – Manual Input found on the internet combined with a self developed video sequentation
> algorithm to preprocess the video. The inputs of the algorithms are going to be optimised for the output of the
> preprocessing algorithm.

## Testing the algorithms

> Since there is no available test data for the algorithm I will use video clips from the internet to test the
> algorithm.

## Milestones

### 2023.02.26

> - Project plan is ready and approved by project leader.
> - All technologies are ready to use, all necessary preparations done.
> - Full understanding of the underlying ideas.

### 2023.03.12

> - Presentation of the results of the bibliography research is ready.
> - Presentation of the used technologies are ready.

### 2023.03.19

> - Image processing algorithm is developed and tested.

### 2023.03.26

> - Implementation of the first algorithm is ready and tested.

### 2023.04.02.

> - Implementation of the second algorithm is ready and tested.

### 2023.04.16.

> - The combination of the two algorithms is developed and tested.

### 2023.04.30.

> - MVP ready.

### 2023.05.07.

> - Documentation and implementation is fully working and ready to pitch.

### 2023.05.14.

> - Demonstration of the product.

## Minimum viable product

> The purpose of the minimum viable product is to show the customers a pre-release product which can also be tested at
> the market.

> The MVP of this project should have the following abilities:
> 1) The image processing is fully working and can turn a video of the road into readable data
> 2) Both of the 2 algorithm can successfully cluster the different road objects on test videos
> 3) The combined algorithm can successfully cluster different road objects on the videos and can plan the best route to
     avoid them with a success rate of 65% 

