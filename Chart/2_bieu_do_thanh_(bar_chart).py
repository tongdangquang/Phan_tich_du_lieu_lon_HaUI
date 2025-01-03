import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter

df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

# chuyển cột "Date" sang kiểu dữ liệu Datetime
df["Date"] = pd.to_datetime(df["Date"])

# vẽ đồ thị cột cho "Volume" theo thời gian
plt.figure(figsize=(12, 6))
plt.bar(df["Date"], df["Volume"], color = "red", label = "Volume")

# đặt thời gian
plt.gca().xaxis.set_major_locator(YearLocator(1)) # đặt khoảng thời gian là 1 năm
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y')) # định dạng nhãn ở trục x chỉ hiển thị năm

# đặt khoảng cho trục y
plt.ylim(0, 400000) # đặt khoảng cho trục y
plt.yticks(range(0, 400001, 50000)) # chia khoảng cho trục y

# điều chỉnh tiêu đề biểu đồ
plt.title("Gold Trading Volume over Time", fontweight = "bold", fontsize = "24")

# điều chỉnh tên các trục
plt.xlabel("Date", fontweight = "bold")
plt.ylabel("Volume", fontweight = "bold")

# điều chỉnh nhãn ở các trục
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)

# phưởng thức legend() để hiển thị chú thích ở góc biểu đồ
plt.legend(loc = "upper left") 

# điều chỉnh lưới trong biểu đồ
plt.grid(color = "black", linestyle = "--", linewidth = 0.2)

plt.show()
