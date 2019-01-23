import bs4 as bs
import requests
import pandas as pd
import numpy as np
from wikiURL import wikiURL
from wikiURL import fighterName
from dfFormat import dfFormat

pd.set_option('display.expand_frame_repr', False)

userinput1 = 'nick diaz'
userinput1 = userinput1.title()
userinput2 = 'anthony johnson'
userinput2 = userinput2.title()

df1 = dfFormat(userinput1)
df2 = dfFormat(userinput2)

mergedFight = pd.merge(df1, df2, on = ['Opponent'])




#doesn't work properly if a fighter has found a shared opponent THREE TIMES (case: Big Nog vs Fedor)
x = 0
for i in mergedFight['Date_x']:

    if x >= len(mergedFight['Date_x']):
        continue
    if x == 0:
        pass
        x+= 1
    elif mergedFight['Date_x'].loc[x] == mergedFight['Date_x'].loc[x-1]:
        mergedFight['Date_x'].loc[x] = '-'
        mergedFight['Method_x'].loc[x] = '-'
        mergedFight['Round_x'].loc[x] = '-'
        mergedFight['Time_x'].loc[x] = '-'
        mergedFight['Result_x'].loc[x] = '-'
        x += 1
    else:
        pass
        x += 1
x = 0
for i in mergedFight['Date_y']:

    if x >= len(mergedFight['Date_y']):
        continue
    if x == 0:
        pass
        x+= 1
    elif mergedFight['Date_y'].loc[x] == mergedFight['Date_y'].loc[x-1]:
        mergedFight['Date_y'].loc[x] = '-'
        mergedFight['Method_y'].loc[x] = '-'
        mergedFight['Round_y'].loc[x] = '-'
        mergedFight['Time_y'].loc[x] = '-'
        mergedFight['Result_y'].loc[x] = '-'
        x += 1
    else:
        pass
        x += 1

mergedFight = mergedFight.set_index('Opponent')

columns = [
           (userinput1, 'Result_x'), (userinput1, 'Method_x'), (userinput1, 'Date_x'), (userinput1, 'Round_x'), (userinput1, 'Time_x'),
           (userinput2, 'Result_y'), (userinput2, 'Method_y'), (userinput2, 'Date_y'), (userinput2, 'Round_y'), (userinput2, 'Time_y')
           ]

mergedFight.columns=pd.MultiIndex.from_tuples(columns)


print(mergedFight)

#have to fix the mergedFight formatting
