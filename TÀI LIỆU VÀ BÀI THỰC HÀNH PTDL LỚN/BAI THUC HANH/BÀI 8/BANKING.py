import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
# Đọc dữ liệu từ tệp banking.txt và tạo DataFrame
df = pd.read_csv("banking.txt", delimiter=",") #đọc dữ liệu của banking.txt, sử dụng dấu , làm ký tự ngăn cách

# Tiền xử lý dữ liệu
### Check missing value
def handel_missing_value(df):
    df_miss = df.columns[df.isna().sum() > 1]
    print(df_miss)
    for i in df_miss:
        print(i)
    ### Chọn các cột dữ liệu số (numeric columns)
    df_numeric = df.select_dtypes(include=['number'])
    print(df_numeric.to_string())
    ###Xóa bỏ các dòng có giá trị khuyết (dù đã kiểm tra qua rằng không có nhưng nên thêm để thành thói quen)
    df_cleaned = df_numeric.dropna()
    return df_cleaned

df_cleaned = handel_missing_value(df)
### Chuẩn hóa theo Z_score normalization
def Z_score_normalize(df_cleaned):
    mean = df_cleaned.mean()
    std_dev = df_cleaned.std()
    
    normalized_data = (df_cleaned - mean) / std_dev
    return normalized_data
data_after_preprocessing = Z_score_normalize(df_cleaned)
print("Z_score normalization :",data_after_preprocessing)
# Lưu dữ liệu đã chuẩn hóa vào một tệp CSV

data_after_preprocessing.to_csv("banking_after_preprocessing.csv", index=False)

# Tạo bảng thống kê (dùng hàm có sẵn tức hàm describe), nếu các bạn muốn đầy đủ thì có thể tạo theo BTH4
data_describe = data_after_preprocessing.describe(include='all')
print(data_describe)

### sử dụng dataset: data_after_preprocessing
def linear_regression_model(data_after_preprocessing):
    # Chọn biến đầu vào (X) và biến mục tiêu (y)
    X = data_after_preprocessing['age'] #biến độc lập
    y = data_after_preprocessing['duration'] #biến phụ thuộc

    X = np.array(X).reshape(-1, 1) #reshape để phù hợp với sklearn( chỉ cần reshape biến độc lập là đủ )
    # Chia dữ liệu thành tập huấn luyện và tập kiểm tra
    #Chia mặc định là tỷ lệ 80-20, tức test_size là 0.2
    #random state =42 quá trình chia dữ liệu sẽ luôn tạo ra kết quả giống nhau, giúp bạn có thể tái lặp được và so sánh kết quả dễ dàng
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Xây dựng mô hình phân tích hồi quy tuyến tính
    model = LinearRegression()

    # Huấn luyện mô hình trên tập huấn luyện
    model.fit(X_train, y_train)

    # Dự đoán kết quả trên tập kiểm tra
    y_pred = model.predict(X_test)

    # Đánh giá mô hình
    rmse =(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    r2 = round(model.score(X_test, y_test), 2) # round là làm tròn 2 số cuối phần thập phân

    
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    # (X_test và y_test) được sử dụng để kiểm tra khả năng dự đoán của mô hình trên dữ liệu mà nó chưa được huấn luyện. Điều này giúp đánh giá hiệu suất của mô hình trên dữ liệu mới và không được sử dụng trong quá trình huấn luyện
    plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
    #X_test trên trục x và các giá trị dự đoán tương ứng từ y_pred trên trục y
    plt.xlabel("Age")
    plt.ylabel("Duration")
    plt.legend()
    plt.show()
    return model, rmse, r2 # đánh giá: nếu rmse nhỏ về 0, r2 lớn về 1 thì mô hình tốt

model_evaluation = linear_regression_model(data_after_preprocessing)
print(model_evaluation)
