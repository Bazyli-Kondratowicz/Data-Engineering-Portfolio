import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

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
    chunk['Randomized_Incident_Number'] = chunk['Randomized_Incident_Number'].astype(str)
    chunk['year'] = chunk['Randomized_Incident_Number'].str[:4]
    chunk['quarter'] = chunk['Randomized_Incident_Number'].str[4:6]
    # limit data for 2020 and Emergency
    chunk = chunk.loc[(chunk.year == '2020') & (chunk.Emergency_Dispatch_Code == 'Emergency')]
    # deop Nan Values in columns used to make calculations
    chunk = chunk.dropna(subset=['On_Scene_Time'])
    chunk = chunk.dropna(subset=['First_In_District'])
    # Convert to proper data type
    chunk.loc[:,'On_Scene_Time'] = pd.to_datetime(chunk['year'] + ' ' + chunk['On_Scene_Time'], format='%Y %H:%M:%S.%f', errors='coerce')
    chunk.loc[:,'Incident_Creation_Time'] = pd.to_datetime(chunk['year'] + ' ' + chunk['Incident_Creation_Time'], format='%Y %H:%M:%S.%f', errors='coerce')
    # Calculate response time in minutes
    chunk.loc[:,'response_time_minutes'] = pd.to_timedelta(chunk['On_Scene_Time'] - chunk['Incident_Creation_Time']).dt.total_seconds() / 60

    #Limit result set only to necessary columns
    return chunk[['Randomized_Incident_Number', 'First_In_District',
       'Emergency_Dispatch_Code', 'Dispatch_Sequence', 'Dispatch_Status',
       'Unit_Type', 'PPE_Level', 'year', 'quarter',
       'response_time_minutes']]
    
def load_to_postgres(df, engine):
    # check if connection is succesful
    with engine.connect() as conn:
        print("Connection successful")
        # load data into table
        try:
            print('Loading...')
            df.to_sql('responses', engine, if_exists='replace', index=False, method='multi')
            conn.commit() # explicitly commit
            print("Data loaded successfully")
        except Exception as e:
                conn.rollback() # explicitly rollback
                print(f"Error loading data: {e}")
    

######

def main():
    data_path = 'data/LAFD_Response_Metrics_-_Raw_Data.csv'

    # create engine
    load_dotenv()
    engine = create_engine(f'postgresql://bkon:{os.getenv('PG_PASSWORD')}!@localhost:5432/postgres')

    chunk_size = 100000
    chunks = []

    for chunk in pd.read_csv(data_path, chunksize=chunk_size):
        processed_chunk = pd.DataFrame(process_chunk(chunk))
        if processed_chunk is not None and not processed_chunk.empty:
            chunks.append(processed_chunk)
    
    # concatenate all chunks into one data frame
    df_filtered = pd.concat(chunks)

    print('Shape of filtered df: ' )
    print(df_filtered.shape)

    load_to_postgres(df_filtered, engine)

main()