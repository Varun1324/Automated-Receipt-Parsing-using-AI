import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David'],
'Age': [25, 30, 35, 40],
'Department': ['HR', 'Engineering', 'Marketing', 'Finance']
}
df = pd.DataFrame(data)
df.to_excel('data.xlsx', index=False)
print("data inserted")