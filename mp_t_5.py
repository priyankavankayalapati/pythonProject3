import pandas as pd
import os
import glob
path = os.getcwd()
csv_files = glob.glob(os.path.join("C:\\Users\\priyankav\\Downloads\\python"))
for f in csv_files:
             df = pd.read_csv(f)
             print('Location:', f)
             print('File Name:', f.split("\\")[-1])
             print('result:')
             display(df)
df1 = pd.read_csv("C:\\Users\\priyankav\\Downloads\\python\\Book 4.csv")
df2 = pd.read_csv("C:\\Users\\priyankav\\Downloads\\python\\Book3.csv")
frames = [df1, df2]
result = pd.concat(frames,ignore_index=True)
display(result)

