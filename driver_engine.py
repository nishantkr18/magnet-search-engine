import pandas as pd
import urllib
from os import path
from glob import glob
import search_engines

def initialize_engines():
    """ Import available engines
        Return list of available engines
    """

    # Manually adding engines here to state priority.
    return [
        search_engines.piratebay(),
        search_engines.torrentscsv(),
        search_engines.rarbg()
    ]

class Engine():
    def __init__(self):
        self.engines = initialize_engines()

    def search(self, **kwargs):
        kwargs['what'] = urllib.parse.quote(kwargs['what'])
        results = []
        for engine in self.engines:
            print('Searching in', engine.name)
            try:
                gen = engine.search(**kwargs)
                for val in gen:
                    results.append(val)
            except Exception as e:
                print(e.__str__())
            if len(results) > 0:
                df = pd.DataFrame.from_dict(results)
                df['size'] = (pd.to_numeric(
                    df['size'].str[:-2])/1024/1024/1024).astype(float).round(2).astype(str) + " GB"
                df['link'] = df['link'].apply(
                    lambda x: f'<a target="_blank" href="{x}">Download</a>')
                df = df[['name', 'size', 'seeds', 'leech', 'link']]
                df = df.astype(
                    {'seeds': 'int32', 'leech': 'int32'}, copy=False)
                df.sort_values(by=['seeds'], ascending=False,
                               inplace=True, ignore_index=True)

                yield df
