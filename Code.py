import numpy as np
from numpy import zeros
import random
import math
from timeit import default_timer

a = []
b = []
S = []

i=0
for i in range(1000):
  a.append(random.uniform(-0.5, 0.5))
for i in range(1000):
  b.append(random.uniform(-0.5, 0.5))

i=0
start = default_timer()
for i in range(1000):
  S.append(((math.sin(a[i]))**2 + (math.cos(b[i]))**2)**0.5)
  S[i]=S[i-1]+S[i]
end = default_timer()
print(end - start)

"""Now I do the same exercise using numpy:"""

a = zeros(1000, float)
b = zeros(1000, float)
S = zeros(1000, float)

i=0
for i in range(1000):
  a[i] = random.uniform(-0.5, 0.5)
for i in range(1000):
  b[i]=random.uniform(-0.5, 0.5)

i=0
start = default_timer()
for i in range(1000):
  S[i]=(((math.sin(a[i]))**2 + (math.cos(b[i]))**2))**0.5
  S[i]=S[i-1]+S[i]
end = default_timer()
print(end - start)
