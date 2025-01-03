import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns


def descriptive (df):
    """
    Hàm tính toán các chỉ số thống kê mô tả cho dữ liệu số trong DataFrame.

    Parameters:
    ----------
    df : pandas.DataFrame
        DataFrame đầu vào cần tính toán thống kê mô tả.

    Returns:
    -------
    None
        In ra bảng thống kê mô tả với các chỉ số sau:
        - Count: Số lượng giá trị
        - Mean: Giá trị trung bình
        - Median: Giá trị trung vị
        - Mode: Giá trị xuất hiện nhiều nhất
        - Min: Giá trị nhỏ nhất
        - Max: Giá trị lớn nhất 
        - Q1: Tứ phân vị thứ nhất (25%)
        - Q2: Tứ phân vị thứ hai (50%)
        - Q3: Tứ phân vị thứ ba (75%)
        - IQR: Khoảng tứ phân vị
        - Variance: Phương sai
        - Stdev: Độ lệch chuẩn

    Notes:
    -----
    - Chỉ xử lý các cột có kiểu dữ liệu số
    - Kết quả được làm tròn đến 2 chữ số thập phân
    - Dữ liệu được hiển thị dưới dạng bảng với các cột là các biến số và các hàng là các chỉ số thống kê
    """
    df_numeric= df.select_dtypes(include=["number"])
    df_count = df_numeric.count()       # count
    df_mean = df_numeric.mean()         # mean
    df_median = df_numeric.median()     # median
    df_mode = df_numeric.mode()         # mode
    df_min = df_numeric.min()           # min
    df_max = df_numeric.max()           # max
    df_Q1 = df_numeric.quantile(0.25)   # Q1
    df_Q2 = df_numeric.quantile(0.5)    # Q2
    df_Q3 = df_numeric.quantile(0.75)   # Q3
    df_IQR = df_Q3 - df_Q1              # IQR
    df_variance = df_numeric.var()      # variance
    df_stdev = df_numeric.std()         # stdev
    # tập hợp các chỉ số thông kê mô tả thành 1 dic
    data = {
        "Count   ": [i for i in df_count],
        "Mean    ": [i for i in df_mean],
        "Median  ": [i for i in df_median],
        "Mode    ": [i for i in df_mode.values[0]],
        "Min     ": [i for i in df_min],
        "Max     ": [i for i in df_max],
        "Q1      ": [i for i in df_Q1],
        "Q2      ": [i for i in df_Q2],
        "Q3      ": [i for i in df_Q3],
        "IQR     ": [i for i in df_IQR],
        "Variance": [i for i in df_variance],
        "Stdev   ": [i for i in df_stdev],
    }
    # chuyển dữ liệu từ dạng dic sang DataFrame
    df_data = pd.DataFrame(data)
    # gán nhãn cho các cột thông qua keys() của dữ liệu số ban đầu
    df_data.index = df_numeric.keys()
    # sử dụng transpose() để chuyển cột thành hàng, hàng thành cột
    des_complete = df_data.transpose()
    # làm tròn giá trị
    des_complete = des_complete.round(2)
    des_complete.to_csv("descriptive.csv")
    print(des_complete.to_string())


# print(df_axis_1.to_csv("describe.csv"))

def missing_data(df):
	data_na = (df.isnull().sum() / len(df)) * 100
	missing_data = pd.DataFrame({ 'Ty le thieu data': data_na })
	print(missing_data)


def check_duplicates(df):
	duplicated_rows_data = df.duplicated().sum()
	print(f"\nSO LUONG DATA BI TRUNG LAP: {duplicated_rows_data}")


# data = df.drop_duplicates()


def line_chart(df, column, title, y_label):
	# Plotting the closing price over time
	plt.plot(df.index, df[column])
	plt.title(title,fontsize=14)
	plt.xlabel('Date',fontsize=14)
	plt.ylabel(y_label,fontsize=14)
	plt.xticks(fontsize=14,rotation=45)
	plt.yticks(fontsize=14)
	
	plt.grid()
	plt.show()


def candlestick_chart(df):
	fig = go.Figure(
		data=[go.Candlestick(
			x=df.index,
			open=df['Open'],
			high=df['High'],
			low=df['Low'],
			close=df['Close_Gold']
		)]
	)
	fig.update_layout(title='Biểu đồ nến vàng', xaxis_title='Date', yaxis_title='Price',font=dict(
			size=18,  # Set the font size here
		))

	# Display the figure
	fig.show()


def bar_chart(df):
	df_volume = [(i - 5000) / (20000 - 5000) for i in df['Volume']]
	# Plotting the trading volume over time with a bar chart
	plt.bar(df.index, df_volume)
	plt.title('Khối lượng giao dịch vàng theo thời gian')
	plt.xlabel('Date')
	plt.ylabel('Volume (*1000)')
	plt.grid()
	plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
	plt.show()


def histogram(df):
	df['Return'] = df['Close_Gold'].pct_change()
	
	# Drop NaN values that result from the percentage change calculation
	stock_data = df.dropna()
	
	# Plotting the histogram of stock returns
	plt.hist(stock_data['Return'], bins=30, edgecolor='black')
	plt.title('Histogram of Gold Stock Returns')
	plt.xlabel('Return')
	plt.ylabel('Frequency')
	plt.show()


def box_plot(df):
	df['Return'] = df['Close_Gold'].pct_change()
	# return = (price_current_day - prev_of_current_day) / prev_of_current_day
	# example: price on 3/3/2000 is 2000, and 2/3/2000 is 1900
	# return = (2000 - 1900) / 1900
	print(df['Return'].describe())
	# Drop NaN values resulting from the percentage change calculation
	stock_data = df.dropna()
	
	# Plotting the box plot of stock returns
	plt.figure(figsize=(8, 6))
	sns.boxplot(y=stock_data['Return'])
	plt.title('Box Plot of Stock Returns')
	plt.xlabel('Return')
	plt.show()



def scatter_plot(df):
    plt.figure(figsize=(10, 6))
    # Vẽ biểu đồ phân tán
    plt.scatter(df['Volume'], df['Close_Gold'], alpha=0.5, color='r', label="Gold Price vs Volume")
    # Đặt tiêu đề và nhãn cho trục
    plt.title('Scatter Plot of Volume vs Close Prices')
    plt.xlabel('Volume (hợp đồng)')
    plt.ylabel('Close Price (USD)')
    # Tùy chỉnh các mốc giá trị trên trục x (Volume) và y (Close)
    plt.xticks(np.arange(0, 400000, 20000))  # Tăng các mốc giá trị trục X từ 0 đến 400 (đơn vị nghìn), cách nhau 10
    plt.yticks(np.arange(1000, 2701, 100))  # Tăng các mốc giá trị trục Y từ 1000 đến 2700, cách nhau 100
    plt.legend()
    plt.grid()
    plt.show()


# ============================ HEATMAP (Bản đồ nhiệt của ma trận tương quan) ============================
def heatmap(df):
    # Tính toán ma trận tương quan
    corr_matrix = df[['Close_Gold', 'Close_SP500', 'Close_Oil', 'Close_DollarIndex']].corr()
    # Vẽ heatmap
    plt.figure(figsize=(6, 4))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title("Correlation Heatmap of Close_Gold, Close_SP500, Close_Oil, Close_DollarIndex")
    plt.show()


# ============================ Moving Average Chart (Biểu đồ trung bình trượt) ============================
def MA_chart(df):
    # Đảm bảo cột 'Date' ở định dạng datetime
    # df['Date'] = pd.to_datetime(df['Date'])

    # Đặt cột 'Date' làm index để dễ dàng vẽ đồ thị
    # df.set_index('Date', inplace=True)

    # Tính trung bình trượt 20 ngày, 100 ngày
    df['MA20'] = df['Close_Gold'].rolling(window=20).mean()
    df['MA100'] = df['Close_Gold'].rolling(window=100).mean()
    df['MA200'] = df['Close_Gold'].rolling(window=200).mean()

    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.plot(df.index, df['Close_Gold'], label='Close Price', color='blue')
    ax.plot(df.index, df['MA20'], label='20-Day MA', color='red')
    ax.plot(df.index, df['MA100'], label='100-Day MA', color='black')
    ax.plot(df.index, df['MA200'], label='200-Day MA', color='green')

    # Đặt tên cho trục và tiêu đề biểu đồ
    plt.title('Gold Price with Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')

    # Hiển thị legend và lưới
    plt.legend()
    plt.grid(True)

    # Lấy các ngày giao dịch đầu tiên của mỗi năm
    first_days_of_year = df.resample('YS').first().index  # Lấy ngày đầu năm

    # Đặt các ngày đầu năm làm nhãn cho trục x
    ax.set_xticks(first_days_of_year)  # Đặt các vị trí cho trục x
    ax.set_xticklabels(first_days_of_year.strftime('%Y-%m-%d'), rotation=45, ha='right')  # Đặt nhãn cho các vị trí

    # Hiển thị biểu đồ
    plt.show()


if __name__ == '__main__':
	df = pd.read_csv('Data_gold_oil_dollar_sp500.csv')
	df["Date"] = pd.to_datetime(df["Date"])  # Chuyển đổi Date sang kiểu datetime
	df.set_index("Date", inplace=True)  # Đặt Date làm index
	missing_data(df)
	check_duplicates(df)
	descriptive(df)
	line_chart(df, "Close_Gold", 'Giá vàng', 'Giá')
	line_chart(df, "DollarIndex", 'Chỉ số DXY', 'Điểm')
	line_chart(df, "SP500", 'Chỉ số SP500', 'Điểm')
	line_chart(df, "Close_Oil", 'Giá dầu', 'Giá')
	box_plot(df)
	histogram(df)
	# candlestick_chart(df)
	MA_chart(df)
	heatmap(df)
	scatter_plot(df)
	