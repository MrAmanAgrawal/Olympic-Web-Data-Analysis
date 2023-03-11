import pandas as pd


def preprocess(data,region_df):
    # filtering for summer olympics
    data = data[data['Season'] == 'Summer']
    # merge with region_df
    data = data.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    data.drop_duplicates(inplace=True)
    # one hot encoding
    data = pd.concat([data, pd.get_dummies(data['Medal'])], axis=1)
    return data