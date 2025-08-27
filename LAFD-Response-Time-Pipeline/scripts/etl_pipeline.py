import pandas as pd

## Defs

# Replace spaces with '_', get rid of text in parenthesis
def clean_columns (df):
    if df is None or df.empty:
        print('Such data frame not exists or is empty')
        return None
    else:
        df.columns = df.columns.str.replace(r' \(.*', '', regex=True)
        df.columns = df.columns.str.replace(' ', '_', regex=False)
    return df

# data needs to be processed in chunks, due to big size of data set ( 7m rows aprox. )
def process_chunk(chunk):
    clean_columns(chunk)
    # extract year and quarter from incident number
    #chunk['Randomized_Incident_Number'] = chunk['Randomized_Incident_Number'].astype(str)
    chunk['year'] = chunk['Randomized_Incident_Number'].str[:4]
    chunk['quarter'] = chunk['Randomized_Incident_Number'].str[4:6]
    # limit data for 2020 and Emergency
    chunk = chunk[(chunk['year'] == '2020') & (chunk['Emergency_Dispatch_Code'] == 'Emergency')]
    return chunk

######

def main():
    #df_test = pd.read_csv('data/LAFD_Response_Metrics_-_Raw_Data.csv', nrows=1000)
    data_path = 'data/LAFD_Response_Metrics_-_Raw_Data.csv'
    chunk_size = 100000
    chunks = []

    for chunk in pd.read_csv(data_path, chunksize=chunk_size, dtype=object):
        processed_chunk = process_chunk(chunk)
        chunks.append(processed_chunk)
    
    df_filtered = pd.concat(chunks)
    print(df_filtered.shape)

main()