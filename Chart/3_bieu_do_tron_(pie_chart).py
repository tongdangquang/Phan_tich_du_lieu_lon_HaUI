import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

# Chuyển cột "Date" sang kiểu dữ liệu Datetime
df["Date"] = pd.to_datetime(df["Date"])

# Đặt các khoảng khối lượng giao dịch
bins = [0, 1000, 10000, 50000, 100000, 150000, 200000, 250000, 300000, df["Volume"].max()] # Định nghĩa các mốc (khoảng) cho khối lượng giao dịch vàng, từ 0 đến giá trị lớn nhất trong cột Volume
labels = ["0-1000", "1001-10000", "10001-50000", "50001-100000", "100001-150000", "150001-200000", "200001-250000", "250001-300000", "300001+"] # Danh sách các nhãn tương ứng với từng khoảng

# Phân loại khối lượng giao dịch vào các khoảng
df["Volume_Range"] = pd.cut(df["Volume"], bins=bins, labels=labels, right=False)

# Tính tổng khối lượng giao dịch cho từng khoảng
volume_by_range = df.groupby("Volume_Range")["Volume"].sum()

# Tạo một danh sách các giá trị explode để tách nhẹ các phần của biểu đồ ra
# explode = [0.01] * len(volume_by_range)  # Mỗi phần tách ra một chút

# Lựa chọn bảng màu tươi tắn 
colors = plt.get_cmap('tab20').colors

# Vẽ biểu đồ tròn với đường nối
plt.figure(figsize=(6, 6))
wedges, texts, autotexts = plt.pie(
    volume_by_range, # dữ liệu để vẽ
    labels=volume_by_range.index, # nhãn của các khoảng khối lượng
    autopct="%1.1f%%", # hiển thị phần trăm và số chữ số sau dấu phẩy (ở đây là 1)
    startangle=140, # góc bắt đầu của biểu đồ, xoay biểu đồ 140 độ để căn chỉnh cho phù hợp
    # explode=explode, # khoảng trống ngăn cách giữa các cung trong biểu đồ
    pctdistance=0.8, # vị trí hiển thị phần trăm trong các phần của biểu đồ
    colors=colors # gán màu sắc cho các cung
)

# Tùy chỉnh nhãn và đường nối từ các cung đến nhãn
for i, text in enumerate(texts):
    x, y = text.get_position() # Lấy vị trí x, y của nhãn.
    plt.annotate( # Thêm các nhãn với đường nối từ mỗi phần biểu đồ tròn ra bên ngoà
        text.get_text(), 
        xy=(x, y), # Vị trí đầu của đường nối
        xytext=(1.3 * x, 1.3 * y), # Đặt nhãn ra xa một chút so với cung
        ha="center", # căn giữa nhãn
        arrowprops=dict(arrowstyle="-", color="gray") # Thiết lập đường nối
    )
    text.set_text("") # Xóa nhãn ban đầu để tránh trùng lặp

# Thêm tiêu đề và hiển thị biểu đồ
plt.title("Percentage of Gold Trading Volume by Range", fontweight="bold", fontsize=16, pad = 35)
plt.show()
