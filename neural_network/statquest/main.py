import numpy as np
from formulas import activation, activation_d, ssr, ssr_d, ssr_db1, ssr_db2\
, ssr_db3, ssr_dw1, ssr_dw2, ssr_dw3, ssr_dw4, predicted_output

x = np.array([0, 0.5, 1])
y = np.array([0, 1, 0])

learning_rate = 0.01
epoch = 999999

w1 = 1
w2 = 1
w3 = 1
w4 = 1

b1 = b2 = b3 = 0

for _ in range(epoch):
  pred = predicted_output(x, w1, w2, b1, b2, w3, w4, b3)

  dw4 = ssr_dw4(pred, y, x, w2, b2)
  dw3 = ssr_dw3(pred, y, x, w1, b1)
  dw2 = ssr_dw2(pred, y, w4, x, b2, w2)
  dw1 = ssr_dw1(pred, y, w3, x, b1, w1)
  
  db1 = ssr_db1(pred, y, w3, b1, w1, x)
  db2 = ssr_db2(pred, y, w4, x, b2, w2)
  db3 = ssr_db3(pred, y)

  b1 -= learning_rate*db1
  b2 -= learning_rate*db2
  b3 -= learning_rate*db3

  w1 -= learning_rate*dw1
  w2 -= learning_rate*dw2
  w3 -= learning_rate*dw3
  w4 -= learning_rate*dw4

print(w1, w2, w3, w4)
print(b1, b2, b3)

