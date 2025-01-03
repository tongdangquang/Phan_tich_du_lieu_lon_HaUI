import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
df = pd.read_csv('weatherHistory.csv')


X = df[['Wind Speed (km/h)', 'Temperature (C)']]  # Tốc độ gió (m/s)
visibility = df['Visibility (km)']  # Tầm nhìn (km)
X = np.array(X)

print(X)
print(X.shape)

#Trong bài này, chúng ta chưa cần chia tệp dữ liệu


# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, visibility)


X1 = float(input("Nhập tốc độ gió:"))
X2 = float(input('Nhập nhiệt độ hiện tại: '))
# Nhập giá trị tốc độ gió mới để dự đoán tầm nhìn
X_new = np.array([[X1, X2]])  # Tốc độ gió mới để dự đoán tầm nhìn
predicted_visibility = model.predict(X_new)

# In ra dự đoán tầm nhìn tương ứng với tốc độ gió mới
print("Dự đoán tầm nhìn là: ", predicted_visibility[0])

