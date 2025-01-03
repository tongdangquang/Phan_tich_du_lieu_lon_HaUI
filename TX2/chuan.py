import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

# câu 1 k có điểm
# câu 2 đọc file
# câu 3 biểu đồ scatter
# câu 4 hồi quy tuyến tính đơn biến
# câu 5 hồi quy tuyến tính đa biến

# Câu 2: đọc file
df = pd.read_csv("banking.txt", delimiter=",")


# Câu 3: vẽ biểu đồ scatter
def scatter_plot(x, y):
    plt.scatter(x, y, color = "blue", label = "Actual")
    plt.title(f"Scatter of {x.name} and {y.name}")
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.legend()
    plt.grid()
    plt.show()

    
# Câu 4: hồi quy tuyến tính đơn biến
def Linear_Reg_don_bien(df):
    x = df["age"]
    y = df["duration"]
    x = np.array(x).reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)

    x_test = float(input(f"Nhập giá trị age muốn dự báo: "))
    y_pred = model.predict([[x_test]])
    print(f"Dự đoán duration với age = {x_test} là: {round(y_pred[0], 2)}")


# Câu 5: hồi quy tuyến tính đa biến
def Linear_Reg_da_bien(df):
    x = df[["age", "duration"]]
    y = df["cons_conf_idx"]
    x = np.array(x)

    model = LinearRegression()
    model.fit(x, y)

    x1 = float(input("Nhập age: "))
    x2 = float(input("Nhâp duration: "))
    x_new = np.array([[x1, x2]])
    y_pred = model.predict(x_new)

    print(f"Result: {y_pred[0]}")


# Câu 6: mô hình train test
def model_LinearReg(df):
    x = df["age"]
    y = df["duration"]
    x = np.array(x).reshape(-1, 1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    # đánh giá mô hình
    rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    rmse2 = metrics.root_mean_squared_error(y_test, y_pred)
    r2 = round(model.score(x_test, y_test), 2)

    plt.scatter(x_test, y_test, color = "blue", label = "Actual")
    plt.plot(x_test, y_pred, color = "red", label = "Predicted")
    plt.title("Scatter of age and duration")
    plt.xlabel("Age")
    plt.ylabel("Duration")
    plt.legend()
    plt.grid()
    plt.show()

    return rmse, rmse2, r2

x, y, z = model_LinearReg(df)