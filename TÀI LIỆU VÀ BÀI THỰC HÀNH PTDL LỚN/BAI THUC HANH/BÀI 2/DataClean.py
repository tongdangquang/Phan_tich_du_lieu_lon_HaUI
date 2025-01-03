import pandas as pd
# đọc file hotel_bookings.csv
df = pd.read_csv('hotel_bookings.csv')
# xóa cột Company
df_drop_company = df.drop(columns=['company'])
#  Chọn các cột dữ liệu số (numeric columns)
df_numeric = df_drop_company.select_dtypes(include=['number'])
# Xóa bỏ các dòng có giá trị khuyết
df_cleaned = df_numeric.dropna()
# Lưu kết quả ra file csv mới với tên hotel_bookings_ok.csv
df_cleaned.to_csv('hotel_bookings_ok.csv ', index=False)  

# đọc file abalone.csv
df_abalone = pd.read_csv('abalone.csv')
# Thay thế các giá trị thiếu bằng giá trị trung bình của cột
df_filled = df_abalone.fillna(df_abalone['Height'].mean())
print(df_filled.to_string())

# để chạy chương trình, gõ ctrl ~ rồi chạy lệnh "python DataClean.py"