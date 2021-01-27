import tensorflow as tf
from skimage import io
import keras
import pandas as pd
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from tensorflow.keras.callbacks import EarlyStopping
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import data
from skimage import filters
from cv2 import cv2 as cv
from PIL import Image, ImageDraw
from math import sqrt
from sklearn.model_selection import train_test_split

trained_model = tf.keras.models.load_model("/home/corentin/Bureau/IA_cloud/ia_cloud/FRANTZ_Corentin/django_faceapp/app_project/saved_model/wordDetectionModel_V0.h5")
#trained_model.summary()

box_kernel = np.array([[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]])


box_kernel2 = np.array([[0 / 9, 0 / 9, 0 / 9, 0 / 9, 0 / 9],
              [0 / 9, 1 / 9, 1 / 9, 1 / 9, 0 / 9],
              [0 / 9, 1 / 9, 1 / 9, 1 / 9, 0 / 9],
              [0 / 9, 1 / 9, 1 / 9, 1 / 9, 0 / 9],
              [0 / 9, 0 / 9, 0 / 9, 0 / 9, 0 / 9]])
              

# Gaussian kernel
gaussian_kernel = np.array([[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                   [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                   [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]])

class_names = ['A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V',
              'W', 'X', 'Y', 'Z']

def convol(image, kernel):


    # Select kernel here:
    kernel = kernel

    # Middle of the kernel
    offset = len(kernel) // 2

    # Create output image
    output_image = np.zeros(np.shape(image))
    draw = ImageDraw.Draw(output_image)

    # Compute convolution between intensity and kernels
    for x in range(offset, input_image.width - offset):
        for y in range(offset, input_image.height - offset):
            acc = [0, 0, 0]
            for a in range(len(kernel)):
                for b in range(len(kernel)):
                    xn = x + a - offset
                    yn = y + b - offset
                    input_pixels=[]
                    pixel = input_pixels[xn, yn]
                    acc[0] += pixel[0] * kernel[a][b]
                    acc[1] += pixel[1] * kernel[a][b]
                    acc[2] += pixel[2] * kernel[a][b]

            draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))

    
        
    
    return output_image

image = io.imread('https://cdn.pixabay.com/photo/2015/09/18/11/37/child-945422_960_720.jpg')
input_image = cv.imread(image)
convolImage = cv.filter2D(image, -1, box_kernel)

imgray = cv.cvtColor(convolImage, cv.COLOR_BGR2GRAY)

# cv.Canny permet d'appliquer des filtres sur l'image
edges = cv.Canny(imgray, 400, 255)

# findContour récupère les positions des coutours et les insère dans un tableau
contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

img = cv.drawContours(imgray, contours, -1, (0, 255,75), 2)

def get_contour_precedence(contour, cols):
    tolerance_factor = 200
    origin = cv.boundingRect(contour)
    return ((origin[1] // tolerance_factor) * tolerance_factor) * cols + origin[0]

contours.sort(key=lambda x:get_contour_precedence(x, img.shape[1]))

array = []
ROI_number = 0
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)
    ROI = imgray[y-3:y+h+3, x-3:x+w+3]
    # bitwise inverse les valeurs des pixels (0->255; 255->0)
    # + passage des valeurs de int à float car notre modèle est entrainé sur float
    ROI = cv.bitwise_not(ROI).astype(np.float32)
    ret,ROI = cv.threshold(ROI,127,255,cv.THRESH_BINARY)
    out = np.array([cv.resize(ROI, (28,28))])
    array.append(out.reshape(28,28,1))
    ROI_number += 1

values = []
for elem in array: 
    values.append(trained_model.predict_classes(elem.reshape(1,28,28,1)))
values

plt.figure(figsize=(10,10))

length = len(array)
for i in range(length):
    value = trained_model.predict_classes(array[i].reshape(1,28,28,1))
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(array[i].reshape(28,28,1), cmap=plt.cm.binary, interpolation='nearest')
    plt.xlabel(class_names[value[0]])
    #print(value[0])
    #print(class_names[value[0]])
    
plt.show()