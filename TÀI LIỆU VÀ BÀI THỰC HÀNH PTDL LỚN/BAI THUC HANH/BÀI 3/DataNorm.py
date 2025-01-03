import pandas as pd
import numpy as np
def read_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Tệp {file_path} không tồn tại.")
        return None
file_path = 'abalone.csv'
dataframe = read_file(file_path) 
if dataframe is not None:
    print(dataframe)

def min_max_normalize(file_path,output_file_path,column):
    df = read_file(file_path)
    min_val = df[column].min()
    max_val = df[column].max()
    df[column] = (df[column] - min_val) / (max_val - min_val)
    # Lưu kết quả vào tệp CSV mới
    df.to_csv(output_file_path, index=False)
    return df


def unit_normalize(file_path,output_file_path,column):
    df = read_file(file_path)
    # Tính tổng bình phương của cột
    sum_squared = np.sum(df[column] ** 2)
    # Chuẩn hóa L2 cột bằng cách chia cho căn bậc hai của tổng bình phương
    df[column] = df[column] / np.sqrt(sum_squared)
    # Lưu kết quả vào tệp CSV mới
    df.to_csv(output_file_path, index=False)
    return df
def Z_score_normalize(file_path,output_file_path,column):
    df = read_file(file_path)
    mean = df[column].mean()
    std_dev = df[column].std()
    
    df[column] = (df[column] - mean) / std_dev
    # Lưu kết quả vào tệp CSV mới
    df.to_csv(output_file_path, index=False)
    return df


file_path = 'abalone.csv'
output_file_path_min_max = 'MinMax.csv'
output_file_path_unit = 'Unit.csv'
output_file_path_z_score = 'Zscore.csv'


read_file(file_path)
print("Min-Max normalization \n",min_max_normalize(file_path,output_file_path_min_max,'Height'))
print("Unit normalization \n",unit_normalize(file_path,output_file_path_unit,'Height'))
print("Z_score normalization \n",Z_score_normalize(file_path,output_file_path_z_score,'Height'))
#Ở bài này, lựa chọn chuẩn hóa theo cột "Height" , vì đề bài yêu cầu chuẩn hóa cho 1 cột kiểu số thực