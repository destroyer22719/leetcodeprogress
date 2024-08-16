import numpy as np


# samples = [np.random.randint(0, 50, [1,2]) for _ in range(3)]

samples = [[0.5, 1.4], [2.3, 1.9], [2.9, 3.2]]

# for i in range(len(samples)):
#   val =  np.random.randint(0, 10, [1,2])
#   print(val)
#   samples[i] = list(val)
print(samples)

# The gradient is 
# def cost_function(X, m, b):
#   total = 0

#   for i in range(len(X)):
#     total += (X[i][1] - (m*X[i][0] + b))**2
#   return total/len(X)

def cost_function_deriv_b(X, m, b):
  total = 0
  for i in range(len(X)):
    total += -2*(X[i][1] - (m*X[i][0] + b))
  return total   

def cost_function_deriv_m(X, m, b):
  total = 0
  for i in range(len(X)):
    total += -2*X[i][0]*(X[i][1] - (m*X[i][0] + b))
  return total   

b = -1
learning_rate = 0.01
m = 2

step_size_b = 1
step_size_m = 1


epoch = 0

while (abs(step_size_b) > 0.0001 and abs(step_size_m) > 0.0001 and epoch < 100000):
  step_size_b = learning_rate*cost_function_deriv_b(samples, m, b)
  step_size_m = learning_rate*cost_function_deriv_m(samples, m, b)

  b = b - step_size_b
  m = m - step_size_m
  epoch += 1


# while step_size_m > 0.001:
#   m = m - learning_rate*step_size_m
#   step_size_m = cost_function_deriv_m(samples, m, b)

print(samples)
print(m, b)