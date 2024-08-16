import numpy as np

a = np.zeros((4,3))
b = np.ones((4,1))

print(a.shape)

c = np.zeros((3,4))
print(c.shape)
print(b.shape)

for i in range(3):
  for j in range(4):
    c[i][j] = a[j][i] + b[j]
  
print(c)
print(a.T+b.T)