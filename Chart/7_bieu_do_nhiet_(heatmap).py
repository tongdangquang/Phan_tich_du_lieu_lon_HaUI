import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

# Khởi tạo kích thước cho biểu đồ
plt.figure(figsize=(8, 6))

# Tính toán ma trận tương quan
corr_matrix = df[['Close_Gold', 'Close_SP500', 'Close_Oil', 'Close_DollarIndex']].corr()
# corr() tính toán ma trận tương quan giữa các cột Close_Gold, Close_SP500, Close_Oil, và Close_DollarIndex. Kết quả là một DataFrame với hệ số tương quan giữa các cặp cột.
# Hệ số tương quan dao động từ -1 đến 1:
    # 1: Mối tương quan dương hoàn hảo (cả hai biến tăng/giảm cùng nhau).
    # -1: Mối tương quan âm hoàn hảo (một biến tăng thì biến kia giảm).
    # 0: Không có tương quan.

# vẽ heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
# annot=True: hiển thị giá trị tương quan trong từng ô
# cmap = "coolwarm": sử dụng bảng màu "coolwarm", màu xanh lam và đỏ hiển thị cho mối tương quan âm và dương
# linewidth: độ dày đường viền giữa các ô

plt.title("Correlation Heatmap of Close_Gold, Close_SP500, Close_Oil, Close_DollarIndex", fontweight = "bold", pad=20)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 8)

plt.show()
