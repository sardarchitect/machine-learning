import numpy as np
import utilities

def linear(x, input_size, output_size):
    weight = np.random.randn(output_size, input_size)
    bias = 0
    return utilities.sigmoid(np.dot(weight, x) + bias)