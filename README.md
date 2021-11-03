# Table of contents
- [Introduction](#introduction)
- [Papers to read](#paragraph1)
- [Project Phases](#paragraph2)


# Introduction <a name="introduction"></a>

**Key Point Detection and Graph Clustering: Multi-Human Pose Estimation**

**Team Members** : Jue Guo, Veer Bains, and Karlis Berkolds

All the members in the team are dedicated to make learning computer vision a fun process, this project can also be used for anyone who attempts to learn machine learning, deep learning and computer
vision with no prior knowledge. However, unlike many other resources, which do not dabble much in math. This project will have a more academic approach.

Multi-person pose estimation aims at localizing 2d key points of an unknown number of people
in an image. It has attracted much research interest because of its significance in various
real-world applications, such as human behavior understanding, human-computer interaction,
and action recognition. This can either be done by first detecting each human and then
predicting their key points (top-down) or predicting all key points and then grouping them into
separate objects(bottom-up). We are interested in the [latter approach](https://arxiv.org/pdf/2007.11864.pdf) and its application of
graph clustering.


## Papers to read ( The list will expand as we try to improve our accuracy) <a name="paragraph1"></a>

* [Simple Baselines for Human Pose Estimation and Tracking](https://openaccess.thecvf.com/content_ECCV_2018/html/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.html)
* [Differentiable Hierarchical Graph Grouping for Multi-Person Pose Estimation](https://openaccess.thecvf.com/content_ECCV_2018/html/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.html)
* [Deep High-Resolution Representation Learning for Human Pose Estimation](https://arxiv.org/pdf/1902.09212.pdf)
* [Dynamic Graph CNN for Learning on Point Clouds](https://arxiv.org/abs/1801.07829)
* [Graph Clustering](https://www.sciencedirect.com/science/article/abs/pii/S1574013707000020) 

## Project Phases  <a name="paragraph2"></a>
**Phase 1**
- Setup train and evaluation scripts for coco and UB-PMC

**Phase 2**
- Implement Differentiable Hierarchical Graph Grouping
- Train and Evaluate on coco keypoints 2017

**Phase 3**
- Explore OHGC for chart analysis
- Train and Evaluate on UB PMC

**Phase 4**
- Hyperparameter search
- Single code repository with a modular structure to plug-n-play different detectors, on different datasets. 
