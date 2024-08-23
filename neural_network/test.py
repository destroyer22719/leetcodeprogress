import numpy as np

print(np.random.randn(2, 1).shape)

l1_weights = np.array([[2.74], [-1.13]])
l1_bias = np.array([[0.0], [0.0]])

l2_weights = np.array([[0.36, 0.63]])
l2_bias = np.array([[0.0]])

print(l1_weights.shape, l1_bias.shape)
print(l2_weights.shape, l2_bias.shape)

