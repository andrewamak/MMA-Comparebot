import bs4 as bs
import requests
import pandas as pd
import numpy as np
from wikiURL import wikiURL
from wikiURL import fighterName
from dfFormat import dfFormat

pd.set_option('display.expand_frame_repr', False)

userinput1 = 'john dodson'
userinput2 = 'demetrious johnson'

df1 = dfFormat(userinput1)
df2 = dfFormat(userinput2)

mergedFight = pd.merge(df1, df2, on = ['Opponent'])


print(mergedFight)


#have to fix the mergedFight formatting
