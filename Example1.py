import pandas as pd

#create a dictionary
webDic = {'Day': [1, 2, 3, 4, 5, 6], 'Visitors': [1000, 2000, 200, 400, 10000, 300], 'Bounce_Rate': [20, 20, 23, 15, 10, 43]}

#create dataframe

df = pd.DataFrame(webDic)

print(df)

'''
Pandas operation : 
1. Slicing
2. joining and merging
3. changing index
4. concatenation
5. data conversion
6. changing column header
'''