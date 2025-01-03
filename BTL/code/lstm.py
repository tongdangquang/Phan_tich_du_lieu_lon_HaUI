import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import mean_squared_error, mean_absolute_error
try:
    df = pd.read_csv("Data_gold_oil_dollar_sp500.csv")
    df["Date"] = pd.to_datetime(df["Date"])  # Chuyển đổi Date sang kiểu datetime
    df.set_index("Date", inplace=True)
except FileNotFoundError:
    print("Error: Data file 'Data_gold_oil_dollar_sp500.csv' not found.")
    exit(1)
except Exception as e:
    print(f"Error loading data: {str(e)}")
    exit(1)
data_filtered = df[['SP500', 'Close_Oil', 'DollarIndex', 'Close_Gold']].dropna()

# Chuẩn hóa dữ liệu
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data_filtered)

# Chia thành tập train/test (80% train, 20% test)
train_size = int(len(data_scaled) * 0.8)
train_data = data_scaled[:train_size]
test_data = data_scaled[train_size:]


# Tách input (X) và output (y)
def create_sequences(data, time_steps=1):
	X, y = [], []
	for i in range(len(data) - time_steps):
		X.append(data[i:i + time_steps])  # Các cột đầu vào
		y.append(data[i + time_steps, -1])  # Cột đầu ra (Close_Gold)
	return np.array(X), np.array(y)


time_steps = 10  # Sử dụng 10 bước thời gian để dự đoán
X_train, y_train = create_sequences(train_data, time_steps)
X_test, y_test = create_sequences(test_data, time_steps)
# Kích thước tập dữ liệu sau xử lý
X_train.shape, y_train.shape, X_test.shape, y_test.shape
print("Dữ liệu đầu vào (X_train):", X_train[:2])  # In 2 mẫu đầu tiên của tập train
print("Dữ liệu đầu ra (y_train):", y_train[:2])  # In 2 nhãn đầu tiên của tập train
print("Shape của X_train:", X_train.shape)  # In kích thước của X_train
print("Shape của y_train:", y_train.shape)

# Xây dựng mô hình LSTM
model = Sequential([
    # Lớp LSTM đầu tiên với 50 nơ-ron, trả về chuỗi (return_sequences=True)
    LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
    Dropout(0.2),  # Thêm Dropout để giảm overfitting

    # Lớp LSTM thứ hai với 50 nơ-ron, không trả về chuỗi (return_sequences=False)
    LSTM(50, return_sequences=False),
    Dropout(0.2),  # Thêm Dropout để giảm overfitting

    # Lớp Dense với 25 nơ-ron, chuyển đổi đầu ra từ LSTM thành dạng đơn giản hơn
    Dense(25),

    # Lớp Dense đầu ra với 1 nơ-ron, dự đoán giá Close_Gold
    Dense(1)
])

# Biên dịch mô hình
# loss='mean_squared_error': Sử dụng hàm MSE để tính sai số
# optimizer='adam': Sử dụng thuật toán Adam để tối ưu
model.compile(optimizer='adam', loss='mean_squared_error')

# Huấn luyện mô hình với dữ liệu train
# validation_data=(X_test, y_test): Sử dụng tập test để đánh giá trong quá trình huấn luyện
# epochs=20: Số lần lặp huấn luyện toàn bộ dữ liệu
# batch_size=32: Số mẫu xử lý cùng lúc trong mỗi bước lặp
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, batch_size=32, verbose=1)

# Dự đoán với tập test
y_pred = model.predict(X_test)

# Chuyển đổi giá trị dự đoán và thực tế về dạng gốc (không chuẩn hóa)
y_test_original = scaler.inverse_transform(
    np.hstack((np.zeros((y_test.shape[0], 3)), y_test.reshape(-1, 1)))
)[:, -1]
y_pred_original = scaler.inverse_transform(
    np.hstack((np.zeros((y_pred.shape[0], 3)), y_pred))
)[:, -1]

# Tính toán sai số
mae = mean_absolute_error(y_test_original, y_pred_original)
rmse = np.sqrt(mean_squared_error(y_test_original, y_pred_original))

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Hàm dự báo với thời gian tùy chọn

def forecast_next_days(model, last_data, days=10, time_steps=10):
    """
    Dự báo giá trị cho một số ngày nhất định.
    model: Mô hình LSTM đã huấn luyện.
    last_data: Dữ liệu đầu vào (chuỗi thời gian gần nhất, định dạng chuẩn hóa).
    days: Số ngày muốn dự báo (mặc định 10).
    time_steps: Số bước thời gian đầu vào cho mô hình.
    """
    predictions = []  # Danh sách chứa giá trị dự đoán
    current_input = last_data[-time_steps:, :]  # Lấy chuỗi thời gian gần nhất làm đầu vào

    for _ in range(days):
        # Dự đoán giá trị tiếp theo
        predicted = model.predict(current_input[np.newaxis, :, :])[0][0]  # Dự đoán 1 giá trị
        predictions.append(predicted)  # Thêm giá trị dự đoán vào danh sách

        # Cập nhật chuỗi thời gian với giá trị dự đoán
        current_input = np.vstack((current_input[1:], [[predicted, 0, 0, 0]]))  # Đẩy dữ liệu mới vào chuỗi

    # Chuyển đổi giá trị dự đoán về giá trị gốc
    predictions_original = scaler.inverse_transform(
        np.hstack((np.zeros((len(predictions), 3)), np.array(predictions).reshape(-1, 1)))
    )[:, -1]

    return predictions_original

# Dự báo cho 7 ngày (hoặc nhiều hơn)
time_steps = 10  # Bước thời gian đầu vào
last_data = test_data[-time_steps:]  # Lấy dữ liệu cuối của tập test
next_7_days = forecast_next_days(model, last_data, days=7, time_steps=time_steps)
# Vẽ biểu đồ so sánh Actual và Predicted
def plot_actual_vs_predicted(y_actual, y_predicted):
    """
    Vẽ biểu đồ so sánh giá thực tế và giá dự đoán.
    y_actual: Giá trị thực tế (actual values).
    y_predicted: Giá trị dự đoán (predicted values).
    """
    plt.figure(figsize=(12, 6))
    plt.plot(y_actual, label="Actual Prices", color="blue")
    plt.plot(y_predicted, label="Predicted Prices", color="red")
    plt.title("Actual vs Predicted Prices")
    plt.xlabel("Time")
    plt.ylabel("Gold Prices")
    plt.legend()
    plt.grid()
    plt.show()

# Gọi hàm vẽ biểu đồ với tập test
plot_actual_vs_predicted(y_test_original, y_pred_original)
# Hàm vẽ biểu đồ
def plot_predict(current_input, next_7_days):
    """
    Vẽ biểu đồ so sánh dữ liệu hiện tại và dữ liệu dự đoán.
    current_input: Dữ liệu hiện tại (input cuối cùng được sử dụng cho dự đoán).
    next_7_days: Dữ liệu dự đoán trong 7 ngày tới.
    """
    plt.figure(figsize=(14, 7))

    # Vẽ dữ liệu hiện tại (Current input)
    plt.plot(range(len(current_input)), current_input, label="Last time", color="blue", marker='o')

    # Vẽ dữ liệu dự đoán (Next 7 days)
    plt.plot(range(len(current_input), len(current_input) + len(next_7_days)),
             next_7_days, label="Next 7 Days Prediction", color="red", marker='o')
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    # Thêm thông tin biểu đồ
    plt.title("Last time vs Next 7 Days Prediction")
    plt.xlabel("Time")
    plt.ylabel("Gold Prices")
    plt.legend()
    plt.grid()
    plt.show()

# Chuyển đổi last_data về giá trị gốc để vẽ biểu đồ
current_input = scaler.inverse_transform(
    np.hstack((np.zeros((last_data.shape[0], 3)), last_data[:, -1].reshape(-1, 1)))
)[:, -1]
# Vẽ biểu đồ
plot_predict(current_input, next_7_days)
