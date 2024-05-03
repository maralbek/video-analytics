# Cordon Counts Project

## Introduction

Welcome to the Cordon Counts Project, an innovative initiative aimed at automating the way Glasgow City Council evaluates pedestrian and cyclist movements during its annual surveys. Since 2007, these surveys have been used in monitoring active travel patterns. Traditionally, the process involved manual counting at specific locations, posing challenges in terms of frequency and efficiency.

This repository introduces a cutting-edge solution to enhance the accuracy and streamline the counting process through the implementation of an automatic counting algorithm. Leveraging state-of-the-art object detection models and tracking algorithms, our approach presents a paradigm shift from manual to automated counting, offering a more efficient and scalable solution.

In this README file, you'll find comprehensive details about the project, including technical insights into the algorithm and implementation steps. 

## Key Features

- **Object Detection**: Utilizing advanced object detection algorithms to detect images on individual frame

![detection](/images/detection.png)

 
- **Object Tracking**: Utilizing tracking algorithms to track the object through consecutive frames

![tracking](/images/tracking.gif)

  
- **Automated Counting Algorithm**: Utilizing virtual line passing to count the objects passing in both directions

![counting](/images/counting.gif)


Feel free to navigate through the instructions to gain a deeper understanding of our project. 




# Prerequisites


## TensorFlow 2.2.0 GPU Installation Guide

Before proceeding with the installation, check the compatibility table [here](https://www.tensorflow.org/install/source#gpu).


## Start Clean

```bash
sudo apt purge nvidia*
sudo apt remove nvidia-*
sudo rm /etc/apt/sources.list.d/cuda*
sudo apt autoremove && apt autoclean
sudo rm -rf /usr/local/cuda*
```



## Install Dependencies

```bash
sudo apt install -y g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
```

## Add CUDA Repository


```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-key adv
--fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/7fa2af80.pub
echo "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list 
```

## Update and Install Nvidia Driver 440


```bash
sudo apt update
sudo apt install -y nvidia-driver-440
```

## Install CUDA-10.1


```bash
sudo apt-get -o Dpkg::Options::="--force-overwrite" install cuda-10-1 cuda-drivers 
```

## Set CUDA Paths

```bash
echo 'export PATH=/usr/local/cuda-10.1/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
sudo ldconfig
```

## Download and Install Cudnn 7.6.5 for CUDA 10.1


1. Go to [NVIDIA Cudnn](https://developer.nvidia.com/cudnn) and create an account.
2. Download the suitable version from Cudnn Download.
3. Extract the downloaded file (tar -xzvf <filename>).
4. Copy the files into the CUDA directory:


```bash
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-10.1/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-10.1/lib64/
sudo chmod a+r /usr/local/cuda-10.1/lib64/libcudnn*
```

## Restart the PC

Restart your PC to apply the changes.


## Check Installation


```bash
nvidia-smi
nvcc -V
```

## Install Anaconda and Create TF2.2.0 Environment

Follow the instructions [here](https://towardsdatascience.com/tensorflow-gpu-installation-made-easy-use-conda-instead-of-pip-52e5249374bc) :


```bash
conda create --name tf_gpu tensorflow-gpu=2.2.0
```

## Verify GPU Usage
Activate the environment:

```bash
conda activate tf_gpu
```

Check GPU usage:

```bash
nvidia-smi
nvcc -v
python3
>>> import tensorflow as tf
>>> print(tf.test.gpu_device_name())
>>> quit()
```


## Branches
This project employs different branches to leverage various models, each requiring specific libraries for execution. Here's a brief overview of the available branches:

1. master (default branch).
The default branch for general usage.
2. local_GPU.
This branch is tailored for running TensorFlow 2 models on GPU.
3. yolov4_GPU.
Dedicated to running YOLOv4 models on GPU.

## instructions

1. Go to [object_tracking.py](object_tracking.py) file and update paths for the **cap** and **out** variables. Ensure the correct paths for the input and output videos are specified.  

2. Go to [object_tracking.py](object_tracking.py) file and modify the paths for **detection_graph** and **path_to_labels** variables for the model and corresponding labels

3. Go to [object_tracking.py](config_file.py) file and edit the virtual line start and end point. Note that the top-left corner is represented as [0, 0], and the bottom-right corner as [1280, 720]. 

4. Change the object ID to detect object of interest: persons, cyclist, cars, etc. The IDs can be found in the labelmap file.  https://github.com/maralbek/ubdc_videoanalytics/blob/76bd329b7fec34db57b50c35fa7afccb68708ef7/detection_layer.py#L104

5. Run the code using:

```
python object_tracking.py
```

