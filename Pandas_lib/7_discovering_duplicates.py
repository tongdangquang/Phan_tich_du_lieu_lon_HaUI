import pandas as pd
df = pd.read_csv('data.csv')
# 1. tìm hằng trùng lặp
print(df.duplicated()) # true là trùng, false là không trùng

# 2. loại bỏ hàng trùng lặp
df.drop_duplicates(inplace=True)
print(df)