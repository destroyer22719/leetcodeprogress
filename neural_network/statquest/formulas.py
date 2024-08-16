import numpy as np

def activation(x):
  return np.log(1+np.pow(np.e,x))

def activation_d(x):
  return np.pow(np.e,x)/(1+np.pow(np.e,x))

def ssr(pred, obs):
  return np.sum(np.pow(obs - pred, 2))

def ssr_d(pred, obs):
  return -(obs - pred)

def ssr_dw1(pred, obs, w3, input, b1, w1):
  return 2*np.dot(ssr_d(pred, obs)*(w3),activation_d(input*w1+b1)*input)

def ssr_db1(pred, obs, w3, b1, w1, input):
  return 2*np.dot(ssr_d(pred, obs)*(w3),activation_d(input*w1+b1))

def ssr_dw2(pred, obs, w4, input, b2, w2):
  return 2*np.dot(ssr_d(pred, obs)*(w4),activation_d(input*w2+b2)*input)

def ssr_db2(pred, obs, w4, input, b2, w2):
  return 2*np.dot(ssr_d(pred, obs)*(w4),activation_d(input*w2+b2))

def ssr_dw3(pred, obs, input, w1, b1):
  return 2*np.dot(ssr_d(pred, obs),activation(input*w1+b1))

def ssr_dw4(pred, obs, input, w2, b2):
  return 2*np.dot(ssr_d(pred, obs),activation(input*w2+b2))

def ssr_db3(pred, obs):
  return 2*np.sum(ssr_d(pred, obs))

def predicted_output(input, w1, w2, b1, b2, w3, w4, b3):
  act_1 = activation(w1*input + b1)
  act_2 = activation(w2*input + b2)

  return w3*act_1 + w4*act_2 + b3
