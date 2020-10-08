import numpy as np

# Closure definition
def layer(shape, actv):
    def inner(inputs, weights, bias):
        nout = actv(np.matmul(inputs,weights) + bias)
        return nout
    return inner

# User inputs
t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # input to the network

shape1 = [100, 4]
shape2 = [4, 100]

layer1 = layer(shape1, np.tanh) # Define layer 1
layer2 = layer(shape2, np.tanh) # Define layer 2

# Initialize weights and biases
w1 = np.ones(shape1)
w2 = np.ones(shape2)
b1 = np.ones(shape1[1])
b2 = np.ones(shape2[1])

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer

# Output of second layer
print(h2)