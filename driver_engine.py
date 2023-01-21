from search_engines import piratebay, torrentscsv
import pandas as pd

class Engine():
    def __init__(self):
        self.engines = [
            piratebay.piratebay(), 
            torrentscsv.torrentscsv()
        ]

    def search(self, **kwargs):
        results = []
        for engine in self.engines:
            gen = engine.search(**kwargs)
            for val in gen:
                results.append(val)
            df = pd.DataFrame.from_dict(results)
            df['size'] = (pd.to_numeric(df['size'].str[:-2])/1024/1024/1024).astype(float).round(2).astype(str) + " GB"
            df['magnet'] = df['link'].apply(lambda x: f'<a target="_blank" href="{x}">Download</a>')
            df = df[['name', 'size', 'seeds', 'leech', 'magnet']]
            df = df.astype({'seeds': 'int32', 'leech': 'int32'}, copy=False)
            df.sort_values(by=['seeds'], ascending=False, inplace=True, ignore_index=True)

            yield df           
