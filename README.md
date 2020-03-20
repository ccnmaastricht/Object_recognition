# Object_recognition

## Description

![](https://img.shields.io/github/license/ccnmaastricht/Object_recognition)
![](https://img.shields.io/github/issues/ccnmaastricht/Object_recognition)
![](https://img.shields.io/github/forks/ccnmaastricht/Object_recognition)
![](https://img.shields.io/github/stars/ccnmaastricht/Object_recognition)

The images used in this project were generated using Neurorobotics platform (NRP). A simulated icub robot was used to capture the images. The images were captured using icub left (eye) camera. The icub gazes upon objects belonging to 10 object categories. The resulting images were then resampled (distorted) using ganglion cell distributions in the retina.

The resampled images were used to train a convolutional neural network (CNN). The architecture of the CNN is described in 'train_network.m'

## Requirements

Matlab 2019a or higher

## Usage

The pretrained network can be used to recognize the object as follows:

net.classify(image)

The 'train_network.m' can be used to train the network with your own image dataset.
