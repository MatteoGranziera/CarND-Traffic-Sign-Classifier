# Traffic Sign Recognition Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

The Project
---
The goals / steps of this project are the following:
* Load the data set
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


### Data Set Summary & Exploration

[//]: # 'Image References'
[classes_chart]: ./examples/classes_chart.png 'Classes chart'
[processed_img]: ./examples/processed_img.png 'Processing'
[de_signs]: ./examples/traffic_imgs.png 'Traffic Signs'
[image8]: ./examples/placeholder.png 'Traffic Sign 5'

#### 1. Dataset summary

I used the python and pandas library to calculate summary statistics of the traffic
signs data set:

| Description                                            | Value             |
| :----------------------------------------------------- | :---------------- |
| Input                                                  | 32x32x3 RGB image |
| The size of training set is                            | 34799             |
| The size of the validation set is                      | 4410              |
| The size of test set is                                | 12630             |
| The shape of a traffic sign image is                   | (32, 32, 3)       |
| The number of unique classes/labels in the data set is | 43                |

#### 2. Dataset distribution

Here is an exploratory visualization of the data set. It is a bar chart showing how the data is distributed over the classes

![alt text][classes_chart]

### Design and Test a Model Architecture

#### 1. Preprocess

As a first step, I decided to convert the images to grayscale to reduce the amount of inputs by reducing channels of the image.

Here is an example of a traffic sign image before and after grayscaling.

![alt text][processed_img]

I normalized the image data to maintain data near to 0 and simplify the training process

The difference between the original data set and the augmented data set is the following ...

#### 2. Architecture

My final model consisted of the following layers:

|      Layer      |                 Description                 |
| :-------------- | :------------------------------------------ |
|      Input      |              32x32x1 RGB image              |
| Convolution 5x5 | 1x1 stride, valid padding, outputs 28x28x16 |
|      RELU       |     droupout prob 0.8 after if training     |
|   Max pooling   |        5x5 stride, outputs 14x14x16         |
| Convolution 5x5 | 1x1 stride, valid padding, outputs 10x10x64 |
|      RELU       |     droupout prob 0.8 after if training     |
|   Max pooling   |          5x5 stride, outputs 5x5x           |
| Convolution 2x2 | 1x1 stride, valid padding, outputs 4x4x120  |
|      RELU       |     droupout prob 0.8 after if training     |
|   Max pooling   |         2x2 stride, outputs 2x2x120         |
|   Flattening    |                 output 480                  |
| Fully connected |                 output 120                  |
| Fully connected |             output 43 (classes)             |
|     Softmax     |                                             |

#### 3. How you trained my model.

To train the model, I used an adam optimizer and apply 128 samples batch size. To improve the accuracy I repeat the training fo 30 ephocs with a 0.001 lerning rate value.

#### 4. Approach

My final model results were:

- training set accuracy of 0.996
- validation set accuracy of 0.957
- test set accuracy of 0.946

The first architecture was the LeNet but was not enough to get more than 0.89 accuracy.
I tried to use the YUV color space as in this [paper](http://yann.lecun.com/exdb/publis/pdf/sermanet-ijcnn-11.pdf). But with my actual architecture was still under 0.85~0.87 of accuracy. By adding another convolutional layer the accuracy increase. After that I added a dropout to make the recognition more flexible. The accuracy rise the 0.93 accuracy araound the 20th ephoc but i decided leave 30 to consolidate the pattern.


### Test a Model on New Images

#### 1. Choose five German traffic signs on the web

Here are five German traffic signs that I found on Google Maps moving around Hamburg by taking sreenshots.

![alt text][de_signs]

The prediction was pretty accurate.

#### 2. Model's predictions

Here are the results of the prediction:

|        Image         |      Prediction      |
| :------------------: | :------------------: |
|        Yield         |        Yield         |
|      Keep right      |      Keep right      |
|      Road work       |      Road work       |
|       No entry       |       No entry       |
| Speed limit (30km/h) | Speed limit (30km/h) |

The model was able to correctly guess 5 of the 5 traffic signs, which gives an accuracy of 100%. 

#### 3. Probabilities of predictions

The code for making predictions on my final model is located in the 11th cell of the Ipython notebook.

For the first image, the model is has no doubt, and also others images returns similar values on probabilities.

| Probability | Prediction                                   |
| :---------- | :------------------------------------------- |
| 1.000000    | Yield                                        |
| 0.000000    | No vehicles                                  |
| 0.000000    | No passing for vehicles over 3.5 metric tons |
| 0.000000    | Right-of-way at the next intersection        |
| 0.000000    | Ahead only                                   |

But let's se the last one that introduce a little uncertainty on the value of the speed limit.

| Probability | Prediction                               |
| :---------- | :--------------------------------------- |
| 0.911139    | Speed limit (30km/h)                     |
| 0.077434    | Speed limit (50km/h)                     |
| 0.005195    | Speed limit (20km/h)                     |
| 0.001936    | Vehicles over 3.5 metric tons prohibited |
| 0.001237    | Speed limit (80km/h)                     |



