# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 00:01:20 2022

@author: sebag
"""

import numpy as np

l = [1,2,3,4,5,6,7,8,9]

l_array = np.array(l)
matris = l_array.reshape(3,3)


m1 = matris.mean(axis = 0).tolist()
m2 = matris.mean(axis = 1).tolist()
m = matris.mean()
m_l = [m1,m2,m]

v1 = matris.var(axis = 0).tolist()
v2 = matris.var(axis = 1).tolist()
v = matris.var()
v_l = [v1,v2,v]

sd1 = matris.std(axis = 0).tolist()
sd2 = matris.std(axis = 1).tolist()
sd = matris.std()
sd_l = [sd1,sd2,sd]

max1 = matris.max(axis = 0).tolist()
max2 = matris.max(axis = 1).tolist()
maxt = matris.max()
max_l = [max1,max2,maxt]

min1 = matris.min(axis = 0).tolist()
min2 = matris.min(axis = 1).tolist()
mint = matris.min()
min_l = [min1,min2,mint]

sum1 = matris.sum(axis = 0).tolist()
sum2 = matris.sum(axis = 1).tolist()
sumt = matris.sum()
sum_l = [sum1,sum2,sumt]


libro = dict()
libro['mean'] = m_l
libro['variance'] = v_l
libro['standard deviation'] = sd_l
libro['max'] = max_l
libro['min'] = min_l
libro['sum'] = sum_l

libro

if len(l) == 9:
    print(True)
