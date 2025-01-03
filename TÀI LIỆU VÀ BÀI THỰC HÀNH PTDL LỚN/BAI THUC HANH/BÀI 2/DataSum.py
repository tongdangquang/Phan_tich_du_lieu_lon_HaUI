import pandas as pd
import matplotlib.pyplot as plt
# Đọc file hotel_bookings_ok.csv 
df_bookings_ok = pd.read_csv('hotel_bookings_ok.csv')
# đếm các dữ liệu không bị khuyết
data_count = df_bookings_ok.count()
print(data_count)
# Giá trị trung bình 
data_mean = df_bookings_ok.mean()
print(data_mean)
# Độ lệch chuẩn
data_std = df_bookings_ok.std()
print(data_std)
# Min
data_min = df_bookings_ok.min()
print(data_min)
# max
data_max = df_bookings_ok.max()
print(data_max)
 #sử dụng phương thức quantile() kết hợp với phương thức apply() để áp dụng phân vị cho từng cột
quantiles = df_bookings_ok.apply(lambda x: x.quantile([0.25, 0.5, 0.75]))
print("Phân vị Q1, Q2 (Median), và Q3 cho các cột:")
# print(quantiles.to_string())

#matplotlib.pyplot để vẽ biểu đồ
plt.hist(df_bookings_ok['stays_in_week_nights'], bins=5, edgecolor='k')  # 'bins' là số lượng cột dữ liệu trong histogram
# k là thêm đường viền đen
plt.xlabel('Giá trị') # cột x
plt.ylabel('Số lượng') # cột y
plt.title('Histogram cho cột "stays_in_week_nights"')
plt.show()