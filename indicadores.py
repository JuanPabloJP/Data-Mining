import numpy as np

def MA(n, x):
  ma = np.zeros(len(x))
  for i in range(n - 1, len(x)):
    ma[i] = sum(x[i-n + 1:i + 1])/n
  for j in range(n - 1):
    ma[j] = np.mean(ma[n - 1:len(x)])
  return ma

def momentum(x):
  momentum = np.zeros(len(x))
  for i in range(4, len(x)):
    momentum[i] = x[i] - x[i - 4]
  for j in range(4):
    momentum[j] = np.mean(momentum[4:len(x)])

  return momentum

def disparity(n, x):
  disparity = np.zeros(len(x))
  ma = MA(n, x)
  for i in range(len(x)):
    disparity[i] = x[i]/ma[i]
  return disparity

def OBV(v):
  obv = np.zeros(len(v))
  obv[0] = v[0]
  for i in range(1,len(v)):
    if v[i - 1] <= v[i]:
      obv[i] = obv[i - 1] + v[i]
    else:
      obv[i] = obv[i - 1] - v[i]
  return obv

def upsdowns(x):
  ups = np.zeros(len(x))
  for i in range(len(x) - 1):
    if x[i + 1] >= x[i]:
      ups[i] = 1
    else:
      ups[i] = 0
  return ups

def PSY(n, x):
  ups = upsdowns(x)
  psy = np.zeros(len(ups))
  for i in range(n, len(ups)):
    psy[i] = sum(ups[i - n:i])/n
  for i in range(0, n):
    psy[i] = np.mean(psy[n:len(ups)])
  return psy*100

def BIAS(n, x):
  ma = MA(n, x)
  bias = np.zeros(len(x))
  for i in range(len(x)):
    bias[i] = (x[i] - ma[i])/ma[i]
  return bias*100