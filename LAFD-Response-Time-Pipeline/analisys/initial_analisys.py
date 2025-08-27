import pandas as pd
from pathlib import Path

# print('..'/Path.cwd)

df_sample = pd.read_csv('data/LAFD_Response_Metrics_-_Raw_Data.csv', nrows=1000)
print(df_sample.head())