import pandas as pd

#create a dictionary
data1 = {'HPI': [80, 90, 60, 70], 'Int_rate': [2,1,3,4], 'GDP_IND': [50,45,50,53]}
data2 = {'HPI': [80, 90, 60, 70], 'Int_rate': [2,1,3,4], 'GDP_IND': [50,45,50,53]}
#create dataframe
df1 = pd.DataFrame(data1, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame(data2, index=[2001, 2002, 2003, 2004])

#res = pd.merge(df1, df2)
res = pd.merge(df1, df2, on='HPI')

print(res)

