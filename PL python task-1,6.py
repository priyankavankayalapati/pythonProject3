import pandas as pd
from datetime import datetime,date
df=pd.read_csv("C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\dates.csv")
df['Treatment_start'] = pd.to_datetime(df['Treatment_start'],format='%Y%m%d')
df['Treatment_end'] = pd.to_datetime(df['Treatment_end'],format='%Y%m%d')
c_date=date.today()
df['total_time']=(df['Treatment_end']-df['Treatment_start'])
print(df)