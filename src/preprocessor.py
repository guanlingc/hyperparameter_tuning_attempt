import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def scale_data(self, X_train, X_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled
    
    def select_features(self, df: pd.DataFrame):
        X = df.drop('Scam_Call', axis=1)
        y = df['Scam_Call']
        return X, y
    
    def rename_columns(self, df: pd.DataFrame):
        renamed_df = df.rename(columns = {
                    0: 'ID',
                    1: 'Call_Duration',
                    2: 'Call_Frequency',
                    3: 'Financial_Loss',
                    4: 'Flagged_by_Carrier',
                    5: 'Is_International',
                    6: 'Previous_Contact_Count',
                    7: 'Country_Prefix',
                    8: 'Call_Type',
                    9: 'Timestamp',
                    10: 'Device_Battery',
                    11: 'Scam_Call'
                    })
        return renamed_df
    
    def fillna_with_mean(self, df: pd.DataFrame, target_column: str):
        df[target_column] = df[target_column].fillna(df[target_column].mean())
        return df
    
    def replace_value(self, df: pd.DataFrame, target_column: str, og_value: str, new_value: str):
        df[target_column].replace([og_value],[new_value], inplace=True)
        return df
    
    def z_score_scaling(self, df: pd.DataFrame, target_column: str):
        df[target_column] = (df[target_column] - df[target_column].mean()) / df[target_column].std()
        return df
    
    def normalize(self, df: pd.DataFrame, target_column: str):
        df[target_column] = (df[target_column] - df[target_column].min()) / \
                            (df[target_column].max() - df[target_column].min()) 
        return df
    
    def column_split(self, df: pd.DataFrame, target_column: str, split_1: str, split_2: str): 
        df[[split_1, split_2]] = df[target_column].str.split(' ',expand=True)
        return df
    
    def encode_label(self, df: pd.DataFrame, target_column: str):
        label_encoder = LabelEncoder()
        df[target_column] = label_encoder.fit_transform(df[target_column])
        return df
    
    def one_hot_encoding(self, df: pd.DataFrame, target_column: str, drop_catergory: str):
        one_hot_encoding_df = pd.get_dummies(df[target_column])
        one_hot_df = pd.concat([df, one_hot_encoding_df], axis=1)
        encoded_df = one_hot_df.drop(columns = [target_column, drop_catergory])
        return encoded_df
    
    def change_dataype(self, df: pd.DataFrame, target_column: str, category: str):
        df[target_column] = df[target_column].astype(category)
        return df
    
