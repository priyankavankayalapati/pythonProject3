import pandas as pd
df = pd.read_csv("C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\WHO file.csv")
condition = (df['WHO region'].isin(['Americas', 'Europe'])) & (df['Year'].isin([1986, 1989]))
df = df[condition]
print(df[['WHO region', 'Country', 'Beverage Types', 'Display Value']])
print(df['WHO region'].value_counts())