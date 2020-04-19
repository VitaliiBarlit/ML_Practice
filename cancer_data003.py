#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:13:41 2020

@author: vitalii
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
plt.rc('font', family='Verdana')


from sklearn.datasets import load_boston
boston = load_boston()
print('Data array shape for the Boston set: {}, {}'.format(
    boston.data.shape[0], boston.data.shape[1]))

# X, y = mglearn.datasets.load_extended_boston()
# mglearn.plots.plot_knn_classification(n_neighbors=2)


from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs

# X, y = mglearn.datasets.make_forge()
X,y = make_blobs()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)


from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=1)

clf.fit(X_train, y_train)



