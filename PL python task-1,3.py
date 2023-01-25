import pandas as pd
df = pd.read_csv("C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\coalpublic2013.csv")
print(df[df['Labor_Hours'] > 20000])
print("*"*125)
print(df[df['MSHA ID'].isin([102976, 103380])])
print("*"*125)
print(df[df['Mine_Name'].str.startswith('P')])
print("*"*125)