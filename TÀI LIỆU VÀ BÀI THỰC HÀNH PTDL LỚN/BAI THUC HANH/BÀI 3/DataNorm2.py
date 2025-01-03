import pandas as pd
import numpy as np
from sklearn import preprocessing

def unit_norm_nor(data, column):
    col = np.array(data[column]).reshape(-1,1)
    data.loc[:, column]  = preprocessing.normalize(col, norm='l2', axis=0)
    return data

def min_max_nor(data, column):

    col = np.array(data[column]).reshape(-1, 1)
    data.loc[:, column] = preprocessing.MinMaxScaler().fit_transform(col)
    return data

def z_score_nor(data, column):
    col = np.array(data[column]).reshape(-1, 1)
    data.loc[:, column]  = preprocessing.StandardScaler().fit(col).transform(col)
    return data

df = pd.read_csv('abalone.csv')

df_unit_nor = unit_norm_nor(df, 'Height')
df_unit_nor.to_csv('abalon_u.csv')