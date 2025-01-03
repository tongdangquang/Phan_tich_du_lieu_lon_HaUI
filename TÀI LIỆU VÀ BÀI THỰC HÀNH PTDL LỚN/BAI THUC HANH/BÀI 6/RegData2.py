import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#đọc dữ liệu
df = pd.read_csv('Summary of Weather.csv')

# Vẽ đồ thị scatter
plt.scatter(df['MinTemp'], df['MaxTemp'])

# Đặt tiêu đề và nhãn trục
plt.title('Phụ thuộc tuyến tính của MaxTemp vào MinTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
# Hiển thị đường hồi quy tuyến tính (dựa trên mối quan hệ tuyến tính)

coeff = np.polyfit(df['MinTemp'], df['MaxTemp'], 1) # (biến đầu vào, biến phụ thuộc, bậc của đa thức)
plt.plot(df['MinTemp'], coeff[0] * df['MinTemp'] + coeff[1], color='red', linestyle='--')

# Hiển thị biểu đồ
plt.show()

#Một đường hồi quy tuyến tính được vẽ lên đồ thị để thể hiện mối quan hệ tuyến tính 
# giữa hai biến. Mức độ phụ thuộc tuyến tính có thể được suy ra từ hình dạng của đám mây điểm. 
# Nếu các điểm phân bố gần một đường thẳng, thì mối quan hệ giữa hai biến là tuyến tính.