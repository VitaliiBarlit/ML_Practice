#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:32:58 2020

@author: vitalii
"""


import pyautogui
import time
import random as rn
import statistics
import numpy as np
# pyautogui.mouseInfo()

time.sleep(5)
pyautogui.moveTo(480, 648, duration=0.5)
# pyautogui.press(keys, args, kwds)
pyautogui.click()


# pyautogui.dragTo(1200, 108, duration=0.5)
# pyautogui.dragTo(1440, 648, duration=0.5)
# pyautogui.dragTo(480, 648, duration=0.5)
X = []
Y = []
temp = 0
while temp < 100:
    m = rn.randint(200,1400)
    n = rn.randint(200,800)

    pyautogui.click(m, n, duration=0.05)
    X.append(m)
    Y.append(n)
    
    temp += 1
    
# m = [i for i in np.linspace(200, 2*np.pi + 1400, 7)]
# n = [j for j in np.linspace(200, 2*np.pi + 800, 7)]    
# for k in range(7):
#     pyautogui.click(m[k], n[k], duration=0.05)
    
    
print('X mean: {},\nX stdev: {}\n'.format(statistics.mean(X), statistics.stdev(X)))    
print('Y mean: {},\nY stdev: {}\n'.format(statistics.mean(Y), statistics.stdev(Y)))
