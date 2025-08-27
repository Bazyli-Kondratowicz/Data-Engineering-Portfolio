import pandas as pd
from pathlib import Path



df_sample = pd.read_csv('data/LAFD_Response_Metrics_-_Raw_Data.csv', nrows=1000)
print(df_sample.head())
print(df_sample.columns.tolist())
print(df_sample.isnull().sum())

df_sample.columns = df_sample.columns.str.replace(r' \(.*', '', regex=True)
df_sample.columns = df_sample.columns.str.replace(' ', '_', regex=False)
print(df_sample.columns.tolist())

df_sample['Randomized_Incident_Number'] = df_sample['Randomized_Incident_Number'].astype(str)
df_sample['year'] = df_sample['Randomized_Incident_Number'].str[:4]
df_sample['quarter'] = df_sample['Randomized_Incident_Number'].str[4:6]
#print(df_sample.head().dtypes)
#print(df_sample.head())

df_sample = df_sample[df_sample['year'] == '2020']
print(df_sample.head())