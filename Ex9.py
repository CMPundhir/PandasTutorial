import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")
country = pd.read_csv("unemployment_data_world.csv")
d2 = country.set_index("Country Code")
#print(country[10:20])
#print(country[:10])
d2 = d2.head(50)
d3 = d2.reindex(columns=['2010', '2011'])

print(d3)

db = d3.diff(axis=1)
db.plot(kind= 'bar')
plt.show()

