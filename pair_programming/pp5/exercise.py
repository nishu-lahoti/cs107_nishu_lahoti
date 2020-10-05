import numpy as np
import random

class Layer:
    def __init__(self, shape, actv):
        self.weights = np.random.rand(shape[0], shape[1])
        self.bias = np.ones(shape[1])
        self.actv = actv
    
    def __repr__(self):
        return repr("Here is the bias matrix {}").format(self.bias)

    def __str__(self):
         return "The function we're using is {}".format(self.actv)

    def __len__(self):
        return len(self.weights)
    
    def forward(self, inputs):
        output = actv(np.matmul(inputs, self.weights) + self.bias)
        return output


shape1 = [100, 4]
shape2 = [4, 100]
actv = np.tanh
inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)

print(h2)
r = Layer(shape1, actv)
print(repr(r))
print(str(r))
print(len(r))
