#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:01:47 2020

@author: vitalii
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
plt.rc('font', family='Verdana')

X, y = mglearn.datasets.make_forge()
mglearn.discrete_scatter(X[: ,0], X[:, 1], y) # Dispersion plot
plt.legend(['Class 0','Class 1'], loc=4)
plt.xlabel('First feature')
plt.ylabel('Second feature')

print('X array shape: {}'.format(X.shape))

# comment above to see below

X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel('Feature')
plt.ylabel('Target variable')

"""
Target variable, in the machine learning context is the variable that is 
or should be the output. For example it could be binary 0 or 1 if you 
are classifying or it could be a continuous variable if you are doing 
a regression. In statistics you also refer to it as the response variable.
"""

