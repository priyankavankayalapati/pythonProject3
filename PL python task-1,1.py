import pandas as pd
file = "C:\\Users\\priyankav\\Desktop\\Adv's python\\Assignment-1-input_files\\Assignment-1-input_files\\employee.xlsx"
# print(file)
df1 = pd.read_excel(file, sheet_name=0)
df2 = pd.read_excel(file, sheet_name=1)
df3 = pd.read_excel(file, sheet_name=2)
result = pd.concat([df1, df2, df3])
result.to_excel('combined_employee_data.xlsx', index=False)
print("combined_employee_data.xlsx")