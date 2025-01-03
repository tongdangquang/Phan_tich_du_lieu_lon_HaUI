import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

# Chuyển cột "Date" sang kiểu dữ liệu Datetime
df["Date"] = pd.to_datetime(df["Date"])

# đặt kích thước 
plt.figure(figsize=(10, 6))

# Vẽ biểu đồ phân tán
plt.scatter(df['Volume'], df['Close_Gold'], alpha=0.5, color='r', label="Gold Price vs Volume")

# Đặt tiêu đề và nhãn cho trục
plt.title('Scatter Plot of Volume vs Close Prices')
plt.xlabel('Volume (hợp đồng)')
plt.ylabel('Close Price (USD)')
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)

# Tùy chỉnh các mốc giá trị trên trục x (Volume) và y (Close)
plt.xticks(np.arange(0, 400000, 20000))  # Tăng các mốc giá trị trục X từ 0 đến 400 (đơn vị nghìn), cách nhau 10
plt.yticks(np.arange(1000, 2701, 100))  # Tăng các mốc giá trị trục Y từ 1000 đến 2700, cách nhau 100

plt.legend(loc = "upper right")
plt.grid(color = "black", linestyle = "--", linewidth = 0.1, alpha = 1)
plt.show()
