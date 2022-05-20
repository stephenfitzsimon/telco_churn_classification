import pandas as pd

# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer

def prep_telco(df):
    '''Prepares the dataframe by dropping unneeded columns, and dropping the total charges'''
    #drop foreign key columns
    df.drop(columns = ['internet_service_type_id', 'contract_type_id', 'payment_type_id'], inplace=True)
    #this column might only exist in the .csv
    if 'Unnamed: 0' in list(df.columns):
        df.drop(columns = ['Unnamed: 0'], inplace=True)
    #drop the empty total_charges rows
    df = df[df.total_charges != ' ']
    #cast total_charges to float type
    df.total_charges = df.total_charges.astype(float)
    return df

def telco_make_dummies(df):
    '''creates all catagorical columns into encoded columns'''
    #get all catagorical columns
    cat_cols = list(df.select_dtypes('object').iloc[:,1:].columns)
    # make dummy columns
    dummy_df = pd.get_dummies(df[cat_cols], dummy_na = False, drop_first = True)
    df = pd.concat([df, dummy_df], axis = 1)
    return df

def split_telco_data(df):
    '''splits the telco dataframe into train, test and validate subsets'''
    train, test = train_test_split(df, train_size = 0.8, stratify = df.churn, random_state=123)
    train, validate = train_test_split(train, train_size = 0.7, stratify = train.churn, random_state=123)
    return train, test, validate