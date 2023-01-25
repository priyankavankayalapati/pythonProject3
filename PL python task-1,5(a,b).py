# 5(a)
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_csv("C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\coalpublic2013.csv")
# df = df.head(10)
# ax = df.plot(kind='bar', y=[ 'Year','MSHA ID', 'Production', 'Labor_Hours'],figsize=(20,8))
# ax.set_xlabel('comparing year, MSHA ID, Production and Labor_hours of first ten records')
# plt.show()

# 5(b)
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\coalpublic2013.csv")
top_ten_production = df.nlargest(10, 'Production')
top_ten_production.plot(kind='bar', x='MSHA ID', y='Production')
plt.xlabel('MSHA ID')
plt.ylabel('Production')
plt.show()