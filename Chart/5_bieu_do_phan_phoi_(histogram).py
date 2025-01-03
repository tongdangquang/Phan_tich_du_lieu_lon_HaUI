import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

plt.figure(figsize=(6, 4))

# Vẽ biểu đồ histogram cho "Close_Gold"
n, bins , patches = plt.hist(df["Close_Gold"], bins=30, color="gold", edgecolor="black", alpha=1)  # 'bins' là số lượng cột trong biểu đồ

# Đặt tên cho trục và tiêu đề
plt.xlabel("Gold Closing Price", fontweight="bold")
plt.ylabel("Frequency", fontweight="bold")
plt.title("Distribution of Gold Closing Prices", fontweight="bold")

plt.xticks(bins, rotation = 0, fontsize = 7) # thuộc tính rotation dùng để đặt độ nghiêng của nhãn so với trục x (ở đây là nghiêng 0 độ so với x)
plt.yticks(fontsize = 7)

plt.grid(axis='y', linestyle="--", alpha=0.5)  # Hiển thị lưới ngang với axis = "y" và alpha là độ trong suốt nằm trong khoảng (0 -> 1)
plt.show()