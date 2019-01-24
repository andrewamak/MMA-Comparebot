
from UFCdatamerge import mergedFight
from dfFormat import dfFormat
from wikiURL import fighterName

userinput1 = input('Please enter the name of Fighter 1: ')
userinput2 = input('Please enter the name of Fighter 2: ')

try:
    df1 = dfFormat(fighterName(userinput1))
    df2 = dfFormat(fighterName(userinput2))
    print(mergedFight(df1, df2, userinput1, userinput2))
except:
    print('Sorry! Invalid Fighter name(s)')
