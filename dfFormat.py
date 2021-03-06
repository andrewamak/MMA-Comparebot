import pandas as pd
from wikiURL import wikiURL

pd.set_option('display.expand_frame_repr', False)


def dfFormat(userinput):

    search_url = wikiURL(userinput)
    count = 0

    #some fighters are listed as Fighter_Name(fighter) in wikipedia. So this corrects for that.
    def dfGet(search_url, count):
        try:
            wikitables = pd.read_html(search_url, index_col=0, attrs={"class": "wikitable"})
            df = pd.DataFrame(data=wikitables[count])

        except:
            search_url = search_url + """_(fighter)"""
            wikitables = pd.read_html(search_url, index_col=0, attrs={"class": "wikitable"})
            df = pd.DataFrame(data=wikitables[count])

        #Doesn't work for SOME wikitables as fighters like Nick Diaz may their wikitable in the "wrong spot"
        #need to fix that. probably with a try/except clause.


        #formatting
        df.columns = df.iloc[0]
        df.reset_index(level=0, inplace=True)

        del df.index.name
        df.drop(df.index[0], inplace=True)

        return df
    df = dfGet(search_url, count)

    #fighters like Nick Diaz have other wikitables in their wikipedia page (due to BJJ tournaments etc.
    #This runs through the wikipedia page until it finds columns that match what we're looking for

    while list(df.columns.values) != [0, 'Record', 'Opponent', 'Method', 'Event', 'Date', 'Round', 'Time', 'Location', 'Notes']:
        dfGet(search_url, count)
        df = dfGet(search_url,count)
        count += 1

    df["Location"] = df["Location"].ffill()

    #some fighters like Big Nog and Fedor have multiple fights in the same day, so this will correct for that
    for i in df["Event"]:
        if i.isdigit():
            df.iloc[count]["Event"], df.iloc[count]["Round"] = df.iloc[count]["Round"], df.iloc[count]["Event"]
            df.iloc[count]["Time"] = df.iloc[count]["Date"]
            df.iloc[count]["Date"] = df.iloc[count - 1]["Date"]

        else:
            pass

        count += 1

    df = df.drop(columns=["Event", "Location", "Notes", "Record"])
    df = df.rename(columns={0: 'Result'})
    df.columns.name = ''



    return df