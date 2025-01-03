import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('banking.csv')
# print(df.head())
# print(df.isna().sum() > 1)
df_cleaned = df.dropna()
df_numeric = df_cleaned.select_dtypes(include=['number'])
print(df_numeric.head())

# Cau 3:
def scatter_plot(col1, col2):
    column1 = df[col1]
    column2 = df[col2]
    plt.scatter(column1, column2, label='Dữ liệu', color='blue', marker='o')
    plt.title('Biểu đồ Scatter')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.legend()
    plt.show()


# cau 4
def LinearReg_don(col1, col2):
    X1 = df_numeric[col1]
    y = df_numeric[col2]
    X1 = np.array(X1).reshape(-1, 1)
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X1_train, y1_train)
    y1_pred = model.predict(X1_test)
    rmse =(np.sqrt(metrics.mean_squared_error(y1_test, y1_pred)))
    r2 = round(model.score(X1_test, y1_test), 2)
    print(f"rmse: {rmse}")
    print(f"r2:{r2}")
    print(f"PTHQ: y = {round(model.coef_[0], 2)} * x + {round(model.intercept_, 2)}")

# cau 5
X4=df_numeric[["age","pdays","euribor3m"]]
y = df_numeric['duration']
X4_train, X4_test, y4_train, y4_test = train_test_split(X4, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X4_train,y4_train)
y4_pred = model.predict(X4_test)
rmse = (np.sqrt(metrics.mean_squared_error(y4_test,y4_pred)))
r2 = round(model.score(X4_test,y4_test),2)
print(f"rmse: {rmse} r2:{r2}")
print(f"pthq = {model.coef_[0]:.2f} * x1 + {model.coef_[1]:.2f} * x2 + {model.coef_[2]:.2f} * x3 + {model.intercept_:.2f}")
