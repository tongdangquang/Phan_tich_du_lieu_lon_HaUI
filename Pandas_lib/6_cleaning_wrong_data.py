import pandas as pd
df = pd.read_csv('data.csv')

# 1. Xử lý dữ liệu sai bằng cách thay thế bằng một giá trị cụ thể
df.loc[2, 'Duration'] = 45
print(df)

# 2. Đặt ranh giới cho các giá trị
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.loc[x, 'Duration'] = 120
print(df)

# 3. Loại bỏ hàng dữ liệu đó luôn
for x in df.index:
    if df.loc[x, 'Duration'] > 120:
        df.drop(x, inplace=True)
print(df)