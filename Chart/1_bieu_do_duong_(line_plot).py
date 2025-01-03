import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, DateFormatter

df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

# chuyển cột "Date" sang kiểu dữ liệu Datetime
df["Date"] = pd.to_datetime(df["Date"])

# vẽ đồ thị đường cho "Close_Gold" theo thời gian
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Close_Gold"], color = "red", label = "Gold Price", linestyle = "solid")

# đặt thời gian
plt.gca().xaxis.set_major_locator(YearLocator(1)) # đặt khoảng thời gian là 1 năm
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y')) # định dạng nhãn ở trục x chỉ hiển thị năm

# điều chỉnh tiêu đề biểu đồ
plt.title("Gold closing price over time", fontweight = "bold", fontsize = "24")

# điều chỉnh tên các trục
plt.xlabel("Date", fontweight = "bold")
plt.ylabel("Close_Gold Price", fontweight = "bold")

# điều chỉnh nhãn ở các trục
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)
plt.legend(loc = "upper left") # phưởng thức legend() để hiển thị chú thích ở góc biểu đồ

# điều chỉnh lưới trong biểu đồ
plt.grid(color = "black", linestyle = "-.", linewidth = 0.2)
plt.show()