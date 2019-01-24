import bs4 as bs
import requests
import pandas as pd
import numpy as np
from wikiURL import wikiURL
from wikiURL import fighterName
from dfFormat import dfFormat

pd.set_option('display.expand_frame_repr', False)

#change to fightername from wikiURL



def mergedFight(df1, df2, userinput1,userinput2):
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

    userinput1 = fighterName(userinput1)
    userinput2 = fighterName(userinput2)

    columns = [
               (userinput1, 'Result_x'), (userinput1, 'Method_x'), (userinput1, 'Date_x'), (userinput1, 'Round_x'), (userinput1, 'Time_x'),
               (userinput2, 'Result_y'), (userinput2, 'Method_y'), (userinput2, 'Date_y'), (userinput2, 'Round_y'), (userinput2, 'Time_y')
               ]

    mergedFight.columns=pd.MultiIndex.from_tuples(columns)


    if mergedFight.empty:
        print(fighterName(userinput1) + ' and ' + fighterName(userinput2) + ' do not have any shared opponents.')
    else:
        print(mergedFight)

#have to fix the mergedFight formatting

