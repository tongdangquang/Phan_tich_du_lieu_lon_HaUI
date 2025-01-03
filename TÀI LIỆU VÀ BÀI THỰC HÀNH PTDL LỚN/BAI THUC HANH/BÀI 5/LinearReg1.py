import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
df = pd.read_csv('winequality-red.csv')

humidity_input = float(input("Nhập độ ẩm muốn dự báo:"))
# Dữ liệu mẫu (độ ẩm và nhiệt độ)
X = df['volatile acidity']  # Độ ẩm (%)
Y = df['alcohol']  # Nhiệt độ (°C)
X = np.array(X).reshape(-1, 1)  # Reshape để phù hợp với scikit-learn

print(Y.shape)
print(X.shape)
print(X)
print(Y)
#Trong bài này, chúng ta chưa cần chia tệp dữ liệu

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, Y)

# Dự đoán nhiệt độ dựa trên độ ẩm
new_humidity = np.array([[humidity_input]])  # Độ ẩm mới để dự đoán nhiệt độ
predicted_temperature = model.predict(new_humidity)

print(f"Dự đoán nhiệt độ cho độ ẩm {humidity_input}% là:", predicted_temperature[0], "°C")

