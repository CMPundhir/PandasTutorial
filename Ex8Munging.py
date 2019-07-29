import pandas as pd

data = pd.read_csv("Metadata_Country_API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_103656.csv")

print(data)

data.to_html('edu.html')
