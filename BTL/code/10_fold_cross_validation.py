import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import KFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.layers import Input

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


# Tách input (X) và output (y)
def create_sequences(data, time_steps=1):
	X, y = [], []
	for i in range(len(data) - time_steps):
		X.append(data[i:i + time_steps])  # Các cột đầu vào
		y.append(data[i + time_steps, -1])  # Cột đầu ra (Close_Gold)
	return np.array(X), np.array(y)

# Hàm thực hiện 10-fold cross-validation và tạo bảng thống kê
def cross_validate_and_report(data, time_steps, n_splits=10, epochs=20, batch_size=32):
    """
    Thực hiện cross-validation k-fold và tạo báo cáo thống kê về hiệu suất mô hình.

    Parameters:
        data (numpy.ndarray): Dữ liệu đã được chuẩn hóa (scaled data) dùng để huấn luyện và đánh giá
        time_steps (int): Số bước thời gian (độ dài chuỗi) sử dụng cho việc tạo sequences
        n_splits (int, optional): Số lượng fold trong cross-validation. Mặc định là 10
        epochs (int, optional): Số epoch huấn luyện cho mỗi fold. Mặc định là 20
        batch_size (int, optional): Kích thước batch cho quá trình huấn luyện. Mặc định là 32

    Returns:
        pandas.DataFrame: DataFrame chứa kết quả đánh giá cho mỗi fold, bao gồm:
            - Fold: Số thứ tự của fold
            - Mean Squared Error: Sai số bình phương trung bình
            - R2 Score: Hệ số xác định R2
            - Mean Absolute Error: Sai số tuyệt đối trung bình
            Cuối bảng có thêm một dòng "Average" chứa giá trị trung bình của các metrics

    Quy trình:
        1. Chia dữ liệu thành k fold sử dụng KFold
        2. Với mỗi fold:
            - Tạo sequences từ dữ liệu train và validation
            - Xây dựng và huấn luyện mô hình LSTM
            - Dự đoán trên tập validation
            - Tính toán các metrics đánh giá
        3. Tổng hợp kết quả và tính giá trị trung bình

    Note:
        - Hàm này yêu cầu dữ liệu đầu vào đã được chuẩn hóa
        - Sử dụng mô hình LSTM với kiến trúc cố định
        - Kết quả được chuyển về dạng gốc trước khi tính toán metrics
    """

    # Khởi tạo KFold
    kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)

    # Lưu trữ kết quả của các fold
    fold_results = []

    # Duyệt qua từng fold
    for fold, (train_idx, val_idx) in enumerate(kfold.split(data), 1):
        # Tạo dữ liệu train và validation
        train_data = data[train_idx]
        val_data = data[val_idx]

        # Tạo chuỗi thời gian (sequences)
        X_train, y_train = create_sequences(train_data, time_steps)
        X_val, y_val = create_sequences(val_data, time_steps)

        # Xây dựng mô hình
        model = Sequential([
            Input(shape=(X_train.shape[1], X_train.shape[2])),
            LSTM(50, return_sequences=True),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(25),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Huấn luyện mô hình
        model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)

        # Dự đoán trên tập validation
        y_val_pred = model.predict(X_val)

        # Chuyển giá trị dự đoán và thực tế về dạng gốc
        y_val_original = scaler.inverse_transform(
            np.hstack((np.zeros((y_val.shape[0], 3)), y_val.reshape(-1, 1)))
        )[:, -1]
        y_val_pred_original = scaler.inverse_transform(
            np.hstack((np.zeros((y_val_pred.shape[0], 3)), y_val_pred))
        )[:, -1]

        # Tính các chỉ số
        mse = mean_squared_error(y_val_original, y_val_pred_original)
        mae = mean_absolute_error(y_val_original, y_val_pred_original)
        r2 = r2_score(y_val_original, y_val_pred_original)

        # Lưu kết quả của fold
        fold_results.append({'Fold': fold, 'Mean Squared Error': mse, 'R2 Score': r2, "Mean Absolute Error" : mae})

    # Tạo DataFrame từ kết quả
    results_df = pd.DataFrame(fold_results)

    # Thêm dòng trung bình
    avg_row = pd.DataFrame({
    'Fold': ['Average'],
    'Mean Squared Error': [results_df['Mean Squared Error'].mean()],
    'R2 Score': [results_df['R2 Score'].mean()],
    "Mean Absolute Error" : [results_df["Mean Absolute Error"].mean()]
    })

    # Nối dòng trung bình với DataFrame kết quả
    results_df = pd.concat([results_df, avg_row], ignore_index=True)

    print(results_df)
results_df = cross_validate_and_report(data_scaled, time_steps=10, n_splits=10, epochs=10, batch_size=32)
