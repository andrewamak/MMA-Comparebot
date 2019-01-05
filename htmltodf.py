
import pandas as pd





wikitables = pd.read_html(search_url, index_col=0, attrs={"class":"wikitable"})
df = pd.DataFrame(data=wikitables[0])

print(df.tail())