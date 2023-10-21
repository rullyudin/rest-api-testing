import pandas as pd

data = pd.read_csv("merchant.csv")

def data_replaced(df):
    df['merchant_id'] = data['merchant_id'].str.replace('-','$')
    return df

data_final = data_replaced(data)