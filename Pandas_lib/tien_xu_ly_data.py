import pandas as pd
import numpy as np

df = pd.read_csv("banking.csv")

# 1. Xử lý dữ liệu trùng lặp
def xu_ly_trung_lap(df):
    # kiểm tra dữ liệu trùng lặp
    x = df.duplicated().sum()
    # xóa dữ liệu trùng lặp
    df.drop_duplicates(inplace=True)
    return df


# 2. Điền khuyết dữ liệu
def dien_khuyet(df):
    for col in df:
        df[col] = df[col].fillna(df[col].mode().values[0]) # điền khuyết cho từng cột bằng giá trị mode() của chính cột đó
        df[col] = df[col].fillna(df[col].max()) # điền khuyết cho từng cột bằng giá trị max() của cột đó
        # điền khyết tương tự với các giá trị min(), mean(), median() khác
    return df


# 3. Kiểm tra dữ liệu bị khuyết
def check_missing(df):
    # kiểm tra dữ liệu bị khuyết 
    df_miss = df.isna()
    # đếm dữ liệu bị khuyết của từng cột
    df_has_miss = df.isna().sum()
    # đếm dữ liệu bị khuyết của cả bảng
    total_miss = df.isna().sum().sum()
    # kiểm tra xem cột dữ liệu có bị khuyết không (trả về true là có bị khuyết và false là không bị khuyết)
    check_miss = df.isna().any()
    # hiển thị các hàng dữ liệu có giá trị khuyết
    rows_with_miss = df[df.isna().any(axis=1)].count()


# 4. Xóa dữ liệu khuyết
def xoa_khuyet(df):
    # xóa cột dữ liệu bất kỳ
    df.drop(["age", "job"], axis=1, inplace=True)
    # xóa hàng bất kỳ
    df.drop([0, 1, 2], axis=0, inplace=True) # [0, 1, 2] là chỉ số index của hàng cần xóa
    # xóa các hàng có dữ liệu khuyết
    df.dropna(axis=0, inplace=True)
    # xóa các cột có giá trị khuyết
    df.dropna(axis=1, inplace=True)


# 5. Xử lý dữ liệu phi số
def du_lieu_so_va_phi_so(df):
    # giữ lại các cột dữ liệu số và xóa các cột phi số
    df_num = df.select_dtypes(include="number")
    # giữ lại các cột phi số và xóa các cột dữ liệu số
    df_non_num = df.select_dtypes(exclude="number")
    return df_num, df_non_num


