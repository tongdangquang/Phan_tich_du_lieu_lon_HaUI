import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filled_data_gold_oil_dollar_sp500.csv")

data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Close_Gold': pd.Series(range(100)) + 1200  # giá trị giả định
}
df = pd.DataFrame(data)

# Vẽ biểu đồ vùng
plt.figure(figsize=(10, 6))
plt.fill_between(df['Date'], df['Close_Gold'], color="gold", alpha=0.4)  # Vùng bên dưới đường
plt.plot(df['Date'], df['Close_Gold'], color="orange", linewidth=2)      # Đường biểu diễn chính

# Cài đặt nhãn và tiêu đề
plt.xlabel("Date", fontweight="bold")
plt.ylabel("Gold Closing Price", fontweight="bold")
plt.title("Area Chart of Gold Closing Prices Over Time", fontsize=16, fontweight="bold")
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.show()