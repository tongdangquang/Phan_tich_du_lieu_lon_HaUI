import pandas as pd
# đọc file hotel_bookings.csv
df_train = pd.read_csv('train.csv')
# hiển thị
print(df_train.to_string()) 
#  Chọn các cột dữ liệu số (numeric columns)
df_train_numeric = df_train.select_dtypes(include=['number'])
print(df_train_numeric)
# Xóa bỏ các dòng có giá trị khuyết
df_train_cleaned = df_train_numeric.dropna()
print(df_train_cleaned)
# đếm các dữ liệu không bị khuyết
data_train_count = df_train_cleaned.count()
print(data_train_count)
# Giá trị trung bình 
data_train_mean = df_train_cleaned.mean()
print(data_train_mean)
# Độ lệch chuẩn
data_train_std = df_train_cleaned.std()
print(data_train_std)
# Min
data_train_min = df_train_cleaned.min()
print(data_train_min)
# max
data_train_max = df_train_cleaned.max()
print(data_train_max)
 #sử dụng phương thức quantile() kết hợp với phương thức apply() để áp dụng phân vị cho từng cột
data_train_quantiles = df_train_cleaned.apply(lambda x: x.quantile([0.25, 0.5, 0.75]))
print("Phân vị Q1, Q2 (Median), và Q3 cho các cột:")
print(data_train_quantiles.to_string())

import matplotlib.pyplot as plt
#matplotlib.pyplot để vẽ biểu đồ
plt.hist(df_train_cleaned['Survived'], bins=5, edgecolor='k')  # 'bins' là số lượng cột dữ liệu trong histogram
# k là thêm đường viền đen
plt.xlabel('Giá trị') # cột x
plt.ylabel('Số lượng') # cột y
plt.title('Histogram cho cột "Survived"')
plt.show()