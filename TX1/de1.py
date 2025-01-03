import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Đọc dữ liệu lê dataframe
df = pd.read_csv("winequality-red.csv")


# 2. Lập bảng tóm lược dữ liệu
def descriptive(df):
    df_num = df.select_dtypes(include=["number"])
    df_min = df_num.min()
    df_max = df_num.max()
    df_mean = df_num.mean()
    df_median = df_num.median()
    df_q1 = df_num.quantile(0.25)
    df_q2 = df_num.quantile(0.5)
    df_q3 = df_num.quantile(0.75)
    df_iqr = df_q3 - df_q1
    df_var = df_num.var()
    df_stdev = df_num.std()
    data = {
        "Min": [i for i in df_min],
        "Max": [i for i in df_max],
        "Mean": [i for i in df_mean],
        "Median": [i for i in df_median],
        "Q1": [i for i in df_q1],
        "Q2": [i for i in df_q2],
        "Q3": [i for i in df_q3],
        "IQR": [i for i in df_iqr],
        "Variance": [i for i in df_var],
        "Std_dev": [i for i in df_stdev]
    }

    df_data = pd.DataFrame(data)
    df_data.index = df_num.keys()
    df_complete = df_data.transpose()
    print(df_complete.to_string())
    return df_complete


# 3. Vẽ biểu đồ Histogram cho các cột dữ liệu
def draw_hist(df):
    df_num = df.select_dtypes(include=["number"])
    for col in df_num:
        plt.figure(figsize=(8, 6))
        plt.hist(df_num[col], bins = 30, edgecolor = 'black', color = 'red', label=col)
        plt.title(f'Histogram of {col}', fontweight = 'bold', fontsize = 14)
        plt.xlabel(col, fontsize = 10)
        plt.ylabel('Frequency', fontsize = 10)
        plt.legend()
        plt.grid(linestyle = 'solid', linewidth = 0.4)
        plt.show()


# 4. Vẽ biểu đồ box cho các cột dữ liệu
def draw_box_plot(df):
    df_num = df.select_dtypes(include=["number"])
    for col in df_num:
        plt.figure(figsize=(8, 6))
        plt.boxplot(df_num[col], patch_artist=True)
        plt.title(f'Box plot of {col}', fontweight = 'bold', fontsize = 14)
        plt.ylabel(col, fontsize = 10)
        plt.grid(linestyle = 'solid', linewidth = 0.4)
        plt.show()


# 5. Lập bảng mô tả cho ít nhất 3 cột dữ liệu
def descriptive_table(df):
    df_num = df.select_dtypes(include=["number"])
    des_table = df_num.describe(include="all")
    print(des_table)
    return des_table


# 6. Tìm yếu tố ảnh hướng nhất tới chất lượng rượu vang đỏ
def heatmap(df):
    # Tính toán ma trận tương quan
    correlation_matrix = df.corr()
    # Hiển thị hệ số tương quan với cột 'quality'
    data = correlation_matrix['quality'].sort_values(ascending=False)
    print("Hệ số tương quan của các cột với cột \'quality\':")
    print(data)
    print(f"Thuộc tính ảnh hưởng nhất tới chất lượng rượu vang đỏ là: {data.index[1]} với trọng số {data.values[1]}")
    # Vẽ heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Heatmap')
    plt.show()

def find_the_most_influential_feature(df):
    df = df.drop('quality', axis=1) 
    # tạo PCA model
    model = PCA(n_components=1)
    model.fit_transform(df)
    result = pd.Series(model.components_[0], index=df.columns)
    most_influential_feature = result.abs().idxmax()
    print ("Ma trận trọng số của các thành phần chính")
    print(result)
    print(f"Thuộc tính ảnh hưởng nhất tới thành phần chính đầu tiên: {most_influential_feature} (trọng số = {round(result[most_influential_feature], 6)})")
