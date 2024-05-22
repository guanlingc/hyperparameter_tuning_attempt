import pandas as pd
import sqlite3

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def check_data_path(self):
        print('DataPath is ' + self.data_path)
        return self.data_path
    
    def initiate_local_connection(self):
        conn = sqlite3.connect(self.data_path)
        print('Local Connection Successful')

        return conn
    
    def get_data(self, sql_query, conn):   
        cursor = conn.cursor()
        cursor.execute(sql_query)

        # Fetch all the records from SQL query output
        results = cursor.fetchall()
            
        # Convert results into pandas dataframe
        df = pd.DataFrame(results)
        print('Data Successfully Obtained')
        print('The shape of the data is ' + str(df.shape))
        conn.close()
        return df
    

    