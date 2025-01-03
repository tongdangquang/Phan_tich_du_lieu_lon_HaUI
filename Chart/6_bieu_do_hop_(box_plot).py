import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

# Khởi tạo kích thước cho biểu đồ
plt.figure(figsize=(8, 6))

# vẽ biểu đồ hộp cho cột "Close_Gold"
plt.boxplot(df['Close_Gold'], vert = True, patch_artist = True, boxprops = dict(facecolor = "red", color = "black"))
# vert = True: vẽ biểu đồ theo chiều dọc (vert: vertical), nếu False thì sẽ vẽ biểu đồ theo chiều ngang
# patch_artist = True: biểu đồ sẽ được tô màu thay vì chỉ vẽ mỗi đường viền
# boxprops(): tùy chỉnh các tham số trong box
    # facecolor: màu nền của box
    # color: màu viền của box

# đặt tên cho các trục và tiêu đề
plt.title("Box Plot of Gold Closing Prices", fontsize = 20, fontweight = "bold")
plt.ylabel("Gold closing price", fontweight = 16, rotation = 90)

plt.grid(axis="y", linestyle = "--", alpha = 0.7)
plt.show()