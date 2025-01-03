import pandas as pd

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('candy-data.csv')
print(df)
# Xóa cột "competitorname"
df_drop_competitorname=df.drop(columns=['competitorname'], axis=1)
print(df_drop_competitorname)

#Tách dữ liệu thành tập train và tập test:
from sklearn.model_selection import train_test_split
# Chia dữ liệu thành tập train và tập test (70% train, 30% test)
train_data, test_data = train_test_split(df_drop_competitorname, test_size=0.3, random_state=42)
# Hiển thị kích thước của tập train và tập test
print("Số lượng dữ liệu trong tập train:", len(train_data))
print("Số lượng dữ liệu trong tập test:", len(test_data))

#Xây dựng mô hình hồi quy logistic:
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Xác định biến phụ thuộc (chocolate) và biến độc lập (các thuộc tính khác)
X_train = train_data.drop(columns=['volatile acidity'])
y_train = train_data['chocolate']

# Tạo và huấn luyện mô hình hồi quy logistic trên tập train
logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)# Lúc này, logistic_model đã học đc dữ liệu từ train

# Xác định biến phụ thuộc và biến độc lập trên tập test
X_test = test_data.drop(columns=['chocolate'])
y_test = test_data['chocolate']

# Sử dụng mô hình để dự đoán trên tập test
y_pred = logistic_model.predict(X_test)# Sử dụng logistic_model đã học dữ liệu từ tập train để dự báo X_test

# Tính độ chính xác của mô hình trên tập test
accuracy = accuracy_score(y_test, y_pred)

# In ra độ chính xác
print("Độ chính xác của mô hình trên tập test:", accuracy)
