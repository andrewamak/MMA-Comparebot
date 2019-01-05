import pandas as pd
from wikiURL import wikiURL

pd.set_option('display.expand_frame_repr', False)


def dfFormat(userinput):

    search_url = wikiURL(userinput)

    try:
        wikitables = pd.read_html(search_url, index_col=0, attrs={"class": "wikitable"})
        df = pd.DataFrame(data=wikitables[0])

    except:
        search_url = search_url + """_(fighter)"""
        wikitables = pd.read_html(search_url, index_col=0, attrs={"class": "wikitable"})
        df = pd.DataFrame(data=wikitables[0])

    df.columns = df.iloc[0]
    df.reset_index(level=0, inplace=True)



    count = 0

    del df.index.name
    df.drop(df.index[0], inplace=True)
    df["Location"] = df["Location"].ffill()

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
