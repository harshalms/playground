import numpy as np 
import tensorflow as tf 
import matplotlib.pyplot as plt

def gradient_descent(y_actual, y_predicted):
    m = len(y_actual)
    gradient = np.sum((y_actual-y_predicted)/m, axis=0)
    return gradient

def cost_function(y_actual, y_predicted):
    m = len(y_actual)
    cost = np.sum(((y_actual-y_predicted)**2)/(2*m), axis=0)
    return cost

def training(input, output):
    weights = 
    bias = 
    epochs = 10
    ones = np.ones((5,1))
    input = np.hstack((ones, input))
    for i in range(epochs):
        y_predicted = np.dot(input, weights.T)