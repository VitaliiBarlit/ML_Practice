#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 19:03:02 2020

@author: vitalii
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
plt.rc('font', family='Verdana')

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print('Keys cancer: {}'.format(cancer.keys()))
print('Data array shape: {}'.format(cancer.data.shape))
print('Number of samples for each class: {}'.format({
    n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))
print('Feature names: {}'.format(cancer.feature_names))