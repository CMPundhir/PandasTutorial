import pandas as pd

#create a dictionary
webDic = {'Day': [1, 2, 3, 4, 5, 6], 'Visitors': [1000, 2000, 200, 400, 10000, 300], 'Bounce_Rate': [20, 20, 23, 15, 10, 43]}

#create dataframe

df = pd.DataFrame(webDic)

print(df.head(2))
print(df.tail(2))

