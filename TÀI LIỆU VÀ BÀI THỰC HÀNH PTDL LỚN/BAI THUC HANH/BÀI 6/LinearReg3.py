import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
df = pd.read_csv('Summary of Weather.csv')

MinTemp_input = float(input("Nhập nhiệt độ thấp nhất muốn dự báo:"))
# Dữ liệu mẫu (MinTemp và MaxTemp)
MinTemp = df['MinTemp']  # Nhiệt độ thấp nhất (°C)
MaxTemp = df['MaxTemp']  # Nhiệt độ cao nhất (°C)

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
MinTemp = np.array(MinTemp).reshape(-1, 1)  # Reshape để phù hợp với scikit-learn
model.fit(MinTemp, MaxTemp)

# Nhập giá trị MinTemp mới để dự đoán MaxTemp
new_MinTemp = np.array([[MinTemp_input]])  # Nhiệt độ thấp nhất mới để dự đoán nhiệt độ cao nhất
predicted_MaxTemp = model.predict(new_MinTemp)

# In ra dự đoán nhiệt độ cao nhất tương ứng với MinTemp mới
print("Dự đoán nhiệt độ cao nhất cho nhiệt độ thấp nhất", new_MinTemp[0][0], "°C là:", predicted_MaxTemp[0])