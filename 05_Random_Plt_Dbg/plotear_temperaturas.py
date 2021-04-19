# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 02:12:41 2021

@author: Samsung
"""

import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('Temperaturas.npy')
plt.hist(temperaturas,bins = 10)

