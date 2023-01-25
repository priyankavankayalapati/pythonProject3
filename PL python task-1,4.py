import pandas as pd
df = pd.read_excel("C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\Order Details.xlsx")
df = df.dropna(subset=['ord_no', 'customer_id'])
print(df)