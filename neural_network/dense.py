import numpy as np
from layer import Layer

class Dense(Layer):
  def __init__(self, input_size, output_size, weights=None, bias=None):
    # if weights != None and bias != None:
    self.weights = weights
    self.bias = bias
    print(weights.shape, bias.shape)
    # else:
    #   self.weights = np.random.randn(output_size, input_size)
    #   self.bias = np.random.randn(output_size, 1)
    # print(np.random.randn(output_size, input_size).shape, np.random.randn(output_size, 1).shape)
  def forward(self, input):
    self.input = input
    return np.dot(self.weights, self.input) + self.bias

  def backward(self, output_gradient, learning_rate):
    weights_gradient = np.dot(output_gradient, self.input.T)
    input_gradient = np.dot(self.weights.T, output_gradient)
    self.weights -= learning_rate * weights_gradient
    self.bias -= learning_rate * output_gradient

    
    print("weights: ", self.weights)
    print("bias: ", self.bias)
    return input_gradient