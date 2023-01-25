import pandas as pd
df = pd.read_csv("C:\\Users\\priyankav\\Downloads\\Power_distribution_dataset_task4.csv")
rep = df.fillna({'Thermal_Generation' : 0, 'Nuclear_Generation_Actual' : 0,
                 'Hydro_Generation_Actual' : 0,'Nuclear_Generation_Estimated': 0,
                 'Nuclear_Generation_Actual':0})
dflist =['Thermal_Generation','Thermal_Generation_Actual',
         'Nuclear_Generation_Estimated','Nuclear_Generation_Actual',
         'Hydro_Generation_Estimated','Hydro_Generation_Actual']
df['results'] = df[dflist].sum(axis=1)
grp=df.groupby('Region')['results'].max()
d=grp.to_dict()
print(d)
