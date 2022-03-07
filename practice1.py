# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:38:08 2022

@author: seven
"""

import pandas as pd
import numpy as np

s1 = pd.Series(np.arange(0, 5), index = ['I', 'II', 'III', 'IV', 'V'])
s2 = pd.Series(data = [0.1, 12, 'Bristol', 1000], index = ['a', 'b', 'c', 'd'])
#print(s1)
# print()
# print(s2)
# print()

d1 = {'q': 8, 'r': 16, 's': 24} # create dictionary
s3 = pd.Series(d1)
# print(s3)
# print()

# print(s2['b'])
# print(s2.loc['b'])
# print()

# print(s2[['b', 'd']])
# print(s2.loc[['b', 'd']])
# print()

# print(s2[2])
# print(s2.iloc[2])
# print()

# print(s2[[2, 3, 0]])
# print(s2.iloc[[2, 3, 0]])
# print()

d = {'X' : pd.Series(np.arange(0,5), 
                     index = ['cheese', 'wine', 'bread', 'olives', 'gin']),
     'Y' : pd.Series(['Glasgow', 'London', 'Bristol'], 
                     index = ['wine', 'cheese', 'cider'])}
dF = pd.DataFrame(d)
# print(dF)
# print(dF.index)
# print(dF.columns)

# access column
# print(dF['Y']) # or...
# print(dF.Y)

#access row
# print(dF.loc['cheese']) # or...
# print(dF.iloc[1])

#slice multiple rows
# print(dF[0:2])

#rows where X greater than 2
# dF_new = dF[dF['X'] > 2]
# print(dF_new)


NBA = pd.read_csv('NBA_Stats.csv', sep = ',')
# print(type(NBA))

# print(NBA.info())

# Print the first few rows
print(NBA.head())
print(NBA.tail())





