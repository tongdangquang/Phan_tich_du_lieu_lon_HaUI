import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import matplotlib.pyplot as plt

# Tải mô hình và scaler
model = tf.keras.models.load_model("gold_price_model.keras")
scaler = joblib.load("scaler.pkl")

def process_file(file_path, count_date_predict, count_date_step):
    """
    Xử lý file Excel được kéo thả, lấy dữ liệu và dự đoán.
    """
    try:
        # Đọc file Excel
        data = pd.read_csv(file_path)
        required_columns = ['SP500', 'Close_Oil', 'DollarIndex', 'Close_Gold']

        # Kiểm tra các cột cần thiết
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"File Excel phải chứa các cột: {required_columns}")

        # Lọc dữ liệu và chuẩn hóa
        data_filtered = data[required_columns].dropna()
        data_scaled = scaler.transform(data_filtered)

        # Lấy dữ liệu cuối cùng để làm đầu vào dự đoán
        current_input = data_scaled[-count_date_step:, :]  # Bước thời gian gần nhất

        # Dự đoán count_date_predict ngày tiếp theo
        predictions = []
        for _ in range(count_date_predict):
            predicted = model.predict(current_input[np.newaxis, :, :])[0][0]
            predictions.append(predicted)
            current_input = np.vstack((current_input[1:], [[predicted, 0, 0, 0]]))

        # Chuyển giá trị dự đoán về giá trị gốc
        predictions_original = scaler.inverse_transform(
            np.hstack((np.zeros((len(predictions), 3)), np.array(predictions).reshape(-1, 1)))
        )[:, -1]

        # Vẽ biểu đồ
        plot_predictions(data_filtered['Close_Gold'][-count_date_step:].values, predictions_original)

    except Exception as e:
        messagebox.showerror("Error", f"Lỗi khi xử lý file: {str(e)}")

def plot_predictions(current_input, predictions):
    """
    Vẽ biểu đồ dữ liệu hiện tại và dự đoán.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(range(len(current_input)), current_input, label="Current Input (Last days)", color="blue", marker="o")
    plt.plot(
        range(len(current_input), len(current_input) + len(predictions)), predictions,
        label="Predicted (Next days)", color="red", marker="o"
    )
    plt.title("Gold Price Prediction")
    plt.xlabel("Time")
    plt.ylabel("Gold Prices")
    plt.legend()
    plt.grid()
    plt.show()

def open_file():
    """
    Mở hộp thoại chọn file và xử lý file được chọn.
    """
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            count_date_predict = int(predict_entry.get())
            count_date_step = int(step_entry.get())
            process_file(file_path, count_date_predict, count_date_step)
    except ValueError:
        messagebox.showerror("Invalid Input", "Hãy nhập giá trị hợp lệ cho số ngày dự đoán và số bước thời gian.")

# Tạo giao diện với Tkinter
root = tk.Tk()
root.title("Gold Price Prediction App")

# Nhãn hướng dẫn
instruction_label = tk.Label(root, text="Chọn file CSV và nhập thông số dự đoán.", font=("Arial", 12))
instruction_label.pack(pady=10)

# Nhãn và ô nhập cho số ngày dự đoán
predict_label = tk.Label(root, text="Số ngày dự đoán:", font=("Arial", 10))
predict_label.pack()
predict_entry = tk.Entry(root, font=("Arial", 10))
predict_entry.pack(pady=5)
predict_entry.insert(0, "7")  # Giá trị mặc định

# Nhãn và ô nhập cho số bước thời gian
step_label = tk.Label(root, text="Số bước thời gian:", font=("Arial", 10))
step_label.pack()
step_entry = tk.Entry(root, font=("Arial", 10))
step_entry.pack(pady=5)
step_entry.insert(0, "10")  # Giá trị mặc định

# Nút chọn file
open_button = tk.Button(root, text="Chọn file CSV", command=open_file, bg="blue", fg="white", font=("Arial", 12))
open_button.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
