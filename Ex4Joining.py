import pandas as pd

#create a dictionary
data1 = {'Int_rate': [2,1,3,4], 'GDP_IND': [50,45,50,53]}
data2 = {'HPI': [80, 90, 60, 70], 'Unemployment': [7,8,6,5]}
#create dataframe
df1 = pd.DataFrame(data1, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame(data2, index=[2001, 2003, 2004, 2005])

res = df1.join(df2)
res = df1.join(df2, how='outer')

print(res)



'''
syntax: 
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False)

other : DataFrame, Series, or list of DataFrame
Index should be similar to one of the columns in this one. If a Series is passed, its name attribute must be set, and that will be used as the column name in the resulting joined DataFrame.

on : str, list of str, or array-like, optional
Column or index level name(s) in the caller to join on the index in other, otherwise joins index-on-index. If multiple values given, the other DataFrame must have a MultiIndex. Can pass an array as the join key if it is not already contained in the calling DataFrame. Like an Excel VLOOKUP operation.

how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’
How to handle the operation of the two objects.

left: use calling frame’s index (or column if on is specified)
right: use other’s index.
outer: form union of calling frame’s index (or column if on is specified) with other’s index, and sort it. lexicographically.
inner: form intersection of calling frame’s index (or column if on is specified) with other’s index, preserving the order of the calling’s one.
lsuffix : str, default ‘’
Suffix to use from left frame’s overlapping columns.

rsuffix : str, default ‘’
Suffix to use from right frame’s overlapping columns.

sort : bool, default False
Order result DataFrame lexicographically by the join key. If False, the order of the join key depends on the join type (how keyword).



docs : https://pandas.pydata.org/pandas-docs/version/0.24.2/reference/api/pandas.DataFrame.join.html
'''