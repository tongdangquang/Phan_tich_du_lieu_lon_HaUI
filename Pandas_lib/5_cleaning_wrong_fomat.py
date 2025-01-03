import pandas as pd
# 1. to_datetime(): chuyển đổi dữ liệu không ở định dạng datetime sang datetime
df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])
print(df.to_string())

# 2. dropna(): sử dụng dropna() để xóa hàng dữ liệu đó trong trường hợp không có dữ liệu
df.dropna(subset=['Date'], inplace=True)
print(df)