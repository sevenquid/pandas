# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:24:46 2022

@author: seven
"""

import pandas as pd
import numpy as np

s = pd.Series([2**n for n in range(5)], index = ['A', 'B', 'C', 'D', 'E'])
print(s+s)
print(s**2)
print(np.exp(s))
print(s[:4] + s[-4:])

s.C = 'splendid'
print(s)
print(s+s)
# print(s**2)

testB = {'Sara':95,'Jeff':78,'Phil':65}
testA = {'Lauren':45,'Emma':89,'Harriet':55}
testC = {'Sara':85,'Jeff':45,'Phil':39,'Lauren':75,'Emma':66,'Harriet':54}
d = pd.DataFrame([testB,testA,testC], index=['Test B', 'Test A', 'Test C'])
means = d.mean(0, skipna = True)
print(means)

df = pd.DataFrame({'A' : pd.Series([6,2,9], 
                                   index = ['apple', 'banana', 'orange']),
            'B' : pd.Series([9,8,5,7], 
                            index = ['banana','kiwi', 'orange', 'pineapple'])})
df['C'] = df.A + df.B
df['T/F'] = df.C > 6
df.pop('B')
df.insert(0, 'Ccopy', df.C)
df.insert(1, 'A3', df['T/F'][:3])
print(df)
print()

NBA = pd.read_csv('./NBA_Stats.csv', sep = ',')
print(NBA.info())
print('Min =', NBA.player_height.min())
print('Max =', NBA.player_height.max())
print('Mean =', NBA.player_height.mean())
print('sd =', NBA.player_height.std())
print('Tallest player is', NBA.iloc[NBA.player_height.idxmax()].player_name)
print('Shortest player is', NBA.iloc[NBA.player_height.idxmin()].player_name)
print('Difference between their heights is', NBA.player_height.max()-NBA.player_height.min(), 'cm')

NBAslice = NBA[['player_height', 'oreb_pct', 'dreb_pct']]
print(NBAslice.corr())


def best_scorer(year, season):
    slic = NBA[(NBA.draft_year == year) & (NBA.season == season)]
    print('Best scorer was', NBA.iloc[slic.pts.idxmax()].player_name)
best_scorer('2017', '2017-18')

print(NBA.college.value_counts())

