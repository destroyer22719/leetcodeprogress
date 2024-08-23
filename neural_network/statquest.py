import numpy as np

from dense import Dense
from activations import Log, Final

from network import train, predict
from losses import mse, mse_prime, ssr, ssr_d

import matplotlib.pyplot as plt

X = np.reshape([[0], [0.5], [0]], (3, 1, 1))
Y = np.reshape([[0], [1], [0]], (3, 1, 1))

l1_weights = np.array([[2.74], [-1.13]])
l1_bias = np.array([[0.0], [0.0]])

l2_weights = np.array([[0.36, 0.63]])
l2_bias = np.array([[0.0]])

network = [
  Dense(1, 2, l1_weights, l1_bias),
  Log(),
  Dense(2, 1, l2_weights, l2_bias),
  Final()
]

train(network, mse, mse_prime , X, Y, epochs=100000, learning_rate=0.01)

# points = []
# for x in np.linspace(0, 1, 20):
#     for y in np.linspace(0, 1, 20):
#         z = predict(network, [[x], [y]])
#         points.append([x, y, z[0,0]])

# points = np.array(points)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection="3d")
# ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap="winter")
# plt.show()