# -*- coding: utf-8 -*-
"""Assignment 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Iiavx8QaJmwyII9OA9SOVNElp1qwnF_M

# **Assignment 1**

**Abstract**

---



The main purpose of this assignment is to learn how to use lists and $\tt numpy$ function, know the main differences, and determine which function is more efficient. The design of the study included mathematical operation to test each method efficiency. Firstly, it was asked to create lists of random floats. After, I had to compute the sum of a compound function. And than repeat everything using $\tt numpy$ $\tt arrays$. As it turns out, a numpy array actually takes about the same amount of time as lists to execute code.

**Introduction**


---

In this assignment we are aiming to test list method and numpy function method in mathematical purposes. Usually it is assumed that $\tt numpy$ function always performs better than the default functions like lists. The main indicator of performance is time required to execute code. For better assessment of both methods I decided to use completely the same codes except the method of assigning values (list / array). The primary conjecture is that $\tt numpy$ $ \tt array$ will have much lower execution time than lists.

**Methods**


---

In the 1st task of the problem I had to create two Python lists with $N=1000$ entries each, then use the function $\tt random$ and choose the values of the elements at random with a uniform distribution between $-0.5$ and $0.5$.

So, first I import all necessary packages:
"""

import numpy as np
from numpy import zeros
import random
import math
from timeit import default_timer

"""Then, I create two empty lists **a** and **b** and assign them random values in the given range. The third empty list is for sum variable and for now it remains intact."""

a = []
b = []
S = []

i=0
for i in range(1000):
  a.append(random.uniform(-0.5, 0.5))
for i in range(1000):
  b.append(random.uniform(-0.5, 0.5))

"""In the next task it is asked to determine the time taken for computing mathematical problem using lists. I used math module for trigonometric functions and created a list to compute sum of elements in the list. Also, the main purpose of the task is to calculate time elapsed for code compilation. I used $\tt timeit $ module for this goal."""

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

"""**Results**


---

It can be seen that the main hypothesis was refuted, because it takes approximately the same amount of time to execute code both with the numpy and lists. However, I assume that numpy is still more efficient package for science purposes. I have several assumptions for this. First, I think if number of random values was bigger (>100000) the numpy arrays would be much more efficient. Secondly, I think the way of how my code was constructed can be not really skillful.

**Conclusion**


---

The main goal of this work is to demostrate efficiency of methods of lists and numpy arrays in mathematical operations. It was asked to assign random values between $-0.5$ and $0.5$ to lists a and b. Then, a mathematical formula that included square root, squaring, trigonometric functions, and sum, was applyed using those lists. And finally, the same operations had to be performed using numpy arrays. It was found that numpy arrays not always perform better than lists. In my opinion, it would be useful to test the same methods with larger datasets.
"""