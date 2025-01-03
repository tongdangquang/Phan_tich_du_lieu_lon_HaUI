import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('mtcars.csv')

# Lặp qua từng cột của DataFrame và vẽ histogram cho các cột kiểu nguyên
for column in df.select_dtypes(include=['int64']):
    plt.hist(df[column], bins=10, edgecolor='k')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


# Để vẽ biểu đồ hộp, ta cần đưa dữ liệu về dạng số
#  Chọn các cột dữ liệu số (numeric columns)
df_numeric = df.select_dtypes(include=['number'])

for column in df_numeric.columns:
    plt.figure(figsize=(6, 4))  # Kích thước của biểu đồ
    plt.boxplot(df[column])
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)
    plt.grid(True)
    plt.show()

#Vẽ nhiều cột trên một đồ thị, bằng seaborn
plt.figure(figsize=(6, 4))  # Kích thước của biểu đồ
sns.boxplot(x="variable", y="value", data=pd.melt(df_numeric))
plt.show()

#Vẽ nhiều cột trên một đồ thị, bằng pandas + matplotlib
df_numeric = df_numeric.drop(df_numeric.columns[[3]], axis=1)
df_numeric.plot(kind='box')
plt.show()
