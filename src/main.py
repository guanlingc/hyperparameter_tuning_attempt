from data_loader import DataLoader
from preprocessor import DataPreprocessor
from data_cleaner import DataCleaner
from sklearn.model_selection import train_test_split
from logistic_regression_model import LogisticRegressionModel
from xgb_model import XGBModel
from catboost_model import CatBoostModel
from model_exporter import ModelExporter

# Data Extraction from source file
data = DataLoader("data/calls.db")                  # Pass in data path as a string
data.check_data_path()                              # Returns your data path for review
conn = data.initiate_local_connection()             # Attempts to connect  
df = data.get_data(f'SELECT * FROM calls', conn)    # Pass in SQL syntax as a string 
# print(df.info())

data_cleaner = DataCleaner()

cleaned_df = data_cleaner.get_clean_data(df)
correct_df = data_cleaner.change_cleaned_datatype(cleaned_df)

preprocessor = DataPreprocessor()
# Splitting Features
X, y = preprocessor.select_features(correct_df)
# Train_test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Scaling Data
X_train_scaled, X_test_scaled = preprocessor.scale_data(X_train,X_test)

# Model Training
xgb_model = XGBModel()
xgb_model.train(X_train_scaled, y_train)
accuracy = xgb_model.evaluate(X_test_scaled, y_test)
print("xgb_Accuracy:", accuracy)

# Export Model into model folder
# exporter = ModelExporter()
# exporter.export_model(logreg_model, 'logreg base model')


