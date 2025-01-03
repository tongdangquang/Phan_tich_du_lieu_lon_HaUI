import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('winequality-red.csv')
# hiển thị
print(df) 

# Vẽ đồ thị scatter
column1 = df['alcohol']
column2 = df['pH']
plt.scatter(column1, column2, label='Dữ liệu', color='blue', marker='o')
plt.title('Biểu đồ Scatter')
plt.xlabel('Humidity')
plt.ylabel('Temperature (C)')
# Hiển thị chú thích (nếu cần)
plt.legend()

# Hiển thị đồ thị
plt.show()