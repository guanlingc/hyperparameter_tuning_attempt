import pandas as pd
from sklearn.preprocessing import LabelEncoder
from preprocessor import DataPreprocessor


class DataCleaner:
    def __init__(self):
        self.preprocessor = DataPreprocessor()
        self.label_encoder = LabelEncoder()

    def get_clean_data(self, df: pd.DataFrame):
        # Renames columns
        renamed_df = self.preprocessor.rename_columns(df)
        # Drops duplicates
        renamed_df.drop_duplicates(subset='ID', keep ='first', inplace = True)

        upper_lim = renamed_df['Call_Duration'].quantile(.95)
        lower_lim = renamed_df['Call_Duration'].quantile(.05)
        renamed_df[(renamed_df['Call_Duration'] < upper_lim) & (renamed_df['Call_Duration'] > lower_lim)]
        # renamed_df['Call_Type'] = renamed_df.Call_Type.astype('category')

        # Feature_Engineering for Filling Missing Data
        cleaned_df = self.preprocessor.fillna_with_mean(renamed_df, 'Financial_Loss')
        

        # Feature_Engineering for Replacing Values
        cleaned_df = self.preprocessor.replace_value(renamed_df, 'Call_Type', 'Whats App', 'WhatsApp')
        cleaned_df = self.preprocessor.replace_value(renamed_df, 'Country_Prefix', 'MM', '95')
        

        # Feature_Engineering for Scaling
        cleaned_df = self.preprocessor.normalize(renamed_df, 'Call_Duration')
        cleaned_df = self.preprocessor.z_score_scaling(renamed_df, 'Financial_Loss')


        # Feature_Engineering for Timestamp
        cleaned_df = self.preprocessor.column_split(renamed_df, 'Timestamp', 'Date', 'Time')
        cleaned_df['Date'] = pd.to_datetime(cleaned_df['Date'], format="%Y-%m-%d") 
        cleaned_df['Time'] = pd.to_datetime(cleaned_df['Time'])
        #Extracting Year, Month, Day
        cleaned_df['Year'] = cleaned_df['Date'].dt.year
        cleaned_df['Month'] = cleaned_df['Date'].dt.month
        cleaned_df['Day'] = cleaned_df['Date'].dt.day


        cleaned_df['Call_Frequency'] = pd.cut(renamed_df['Call_Frequency'], bins=[0,5,10,15,30], labels=["Low_Calls", "Mid_Calls", "High_Calls", "Very_High_Calls"])
        cleaned_df['Previous_Contact_Count'] = pd.cut(renamed_df['Previous_Contact_Count'], bins=[0,2,4,8], labels=["Low_Contact", "Mid_Contact", "High_Contact"])
        cleaned_df['Month'] = pd.cut(renamed_df['Month'], bins=[0,3,6,9,12], labels=["Q1", "Q2", "Q3","Q4"])

        # Feature_Engineering for Device_Battery
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Device_Battery', 'Not Charging')
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Call_Type', 'WhatsApp')
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Country_Prefix', '1')
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Flagged_by_Carrier', 'Very Suspicious')
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Previous_Contact_Count', 'High_Contact')
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Call_Frequency', 'Very_High_Calls')
        cleaned_df = self.preprocessor.one_hot_encoding(cleaned_df,'Month', 'Q4')

        # Feature_Engineering for Is_International
        cleaned_df['Is_International'] = self.label_encoder.fit_transform(cleaned_df['Is_International'])

        # Feature_Engineering for Scam_Call
        cleaned_df['Scam_Call'] = self.label_encoder.fit_transform(cleaned_df['Scam_Call'])

        


        correct_df = cleaned_df.drop(columns= ['ID','Timestamp','Date','Time'])

        # print(cleaned_df['Call_Type'].unique())
        # print(cleaned_df['Country_Prefix'].unique())
        # print(correct_df.info())
        return correct_df
    
    def change_cleaned_datatype(self, df: pd. DataFrame):
        
        new_datatype_df = self.preprocessor.change_dataype(df, 'Charging', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Fully Charged', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Suspicious', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Unlikely', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Landline', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Mobile', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Telegram', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Voip', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, '44', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, '65', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, '7', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, '91', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, '95', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Low_Contact', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Mid_Contact', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Low_Calls', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Mid_Calls', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'High_Calls', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Q1', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Q2', 'category')
        new_datatype_df = self.preprocessor.change_dataype(df, 'Q3', 'category')


       
        return new_datatype_df