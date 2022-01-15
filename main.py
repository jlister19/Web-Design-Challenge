import pandas as pd

citiesfile = "Resources/cities.csv"

load = pd.read_csv(citiesfile)

load.to_html('Data.html')
