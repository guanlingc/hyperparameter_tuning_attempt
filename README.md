# aiap17-Chan-Guan-Ling-162D
E-mail Address: chan.guanling@gmail.com

1. data - Storage location for dataset
2. model - Storage location for .pkl file and target location for trained model export
3. src - source code with python classes and functions
    * data_loader.py - pass in data path and use `get_data()` to load in a pandas dataframe 
    * preprocessor.py - class that contains all functions used to process data
    * data_cleaner.py - a function to documents entire data cleaning and feature engineering steps. 
    * logistic_regression_model - Class for training a Logistic Regression Model
    * xgb_model - Class for training a XGBoost Model
    * catboost_model - Class for traing a CatBoost Model
    * model_exporter.py - class to create a folder and export trained models as a .pkl file
    * main.py - Main pipeline

### Flow of pipeline 
##### Data preparation
1. Data is extracted from 'data' folder via _DataLoader_
2. Data is passed onto _DataCleaner_ for all feature engineering using `.get_clean_data`
   * All feature engineering steps are found in data_cleaner.py
   * Modification for feature engineering should all go under this python script
3. Data converted to appropriate data type via `.change_cleaned_datatype`
4. Data at this stage is ready for model training

##### Model Training
4. Data from data preparation is selected via `.select_features` using _DataPreprocessor_
5. Features undergo a train/test split.
   * ratio of split and random_state can be chosen here
6. After splitting, data is scaled
7. Model is trained using X_test_scaled
8. Model can be exported via `.export_model`using _ModelExporter_
  
|Feature Name|Engineering Performed|
|---|---|
|ID|Used to sieve out duplicates, not used otherwise|
|Call Duration| Removed Outlier and normalized values|
|Call Frequency| Binning of into 4 bins and one hot encoding|
|Financial Loss| Filled missing values with mean|
|Flagged by Carrier| One hot encoding|
|Is International| Label encoding|
|Previous Contact| binned and one hot encoded|
|Country Prefix| Value replacement and one hot encoding|
|Call Type| Value replacement and one hot encoding|
|Timestamp| Extraction into Year,Month,Day and one hot encoding, Month is binned and one hot encoded |
|Device Battery| One hot encoding|
|Scam Call|Label encoding|


Models used should be suitable for a classification problem such as Logistic Regression Model, Catboost and XGBoost
1 model from each type was used to determine if a simpler model (i.e Logistic regression) would be better than a complex model.
Typical trade-offs are computation cost, simpler models take less time and computing resources to complete.
This depends on the nature of deployment intended be it offline or online modes. Will there be changes to upstream processing of data?
Will it change overtime etc?
Accuracy is used to evaluate model and is further supplemented with confusion matrix.
Of the 3 models provided, XG Boost model performs best. 

However the models i used, had alot of features used. So from here i see a 3-fold issue. 
1. Number of features used? Is more always better? information might not be readliy avaliable 
2. What Feature engineering techniques? Each feature can be engineered differently depending on feature and model.
3. Which model should be used? some models are sensitive to feature engineering techniques used.

I understand that this work is lacking in certain areas.

Finally, I would like to thank the AIAP Team for providing technical assessments and providing feedback to help me identify knowledge gaps 
so that i can continue to improve my proficiency in such a task. 
