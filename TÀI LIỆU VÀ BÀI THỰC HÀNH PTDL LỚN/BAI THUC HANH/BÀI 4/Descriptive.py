import pandas as pd

df = pd.read_csv('mtcars.csv')
#  Chọn các cột dữ liệu số (numeric columns)
df_numeric = df.select_dtypes(include=['number'])
print(df_numeric)
#Bởi muốn tính TBC, ta phải chuyển dữ liệu về dạng số

# đếm các dữ liệu không bị khuyết
data_count = df_numeric.count()
print(data_count)
# Tính và in ra trung bình cộng theo hàng (axis=1)
row_means = df_numeric.mean(axis=1)
print("Trung bình cộng theo hàng:")
print(row_means)

# Tính và in ra trung bình cộng theo cột (axis=0)
column_means = df_numeric.mean(axis=0)
print("Trung bình cộng theo cột:")
print(column_means)

# Tính median của từng cột
column_medians = df_numeric.median()

print("Median của từng cột:")
print(column_medians)

# Tính mode của từng cột
column_modes = df_numeric.mode()

print("Mode của từng cột:")
print(column_modes)

# Tính giá trị max của từng cột
column_max = df_numeric.max()
print("Giá trị max của từng cột:")
print(column_max)

# Tính giá trị min của từng cột
column_min = df_numeric.min()
print("\nGiá trị min của từng cột:")
print(column_min)

# Tính Q1, Q2 , Q3 cho từng cột
column_q1 = df_numeric.quantile(0.25)
column_q2 = df_numeric.median()
column_q3 = df_numeric.quantile(0.75)
column_IQR = column_q3 - column_q1
print("Q1 của từng cột:")
print(column_q1)

print("\nMedian của từng cột:")
print(column_q2)

print("\nQ3 của từng cột:")
print(column_q3)

print("\nIQR của từng cột:")
print(column_IQR)

# Tính phương sai của từng cột
column_variances = df_numeric.var()
print("Phương sai của từng cột:")
print(column_variances)

# Tính độ lệch chuẩn của từng cột
column_std_devs = df_numeric.std()
print("\nĐộ lệch chuẩn của từng cột:")
print(column_std_devs)


# Tạo bảng thống kê (tự tạo bảng để giống với bảng đề bài yêu cầu)
def descriptive(data_count,column_min,column_max,column_medians,column_modes,column_q1,column_q2,column_q3,column_IQR,column_variances,column_std_devs):
        data = {'Count': [i for i in data_count ],
                'min': [i for i in column_min ],
                'max': [i for i in column_max ],
                'median': [i for i in column_medians ],
                'mode': [i for i in column_modes.values[0]],
                'Q1': [i for i in column_q1 ],
                'Q2': [i for i in column_q2 ],
                'Q3': [i for i in column_q3 ],
                'IQR': [i for i in column_IQR ],
                'Variance': [i for i in column_variances ],
                'stdev': [i for i in column_std_devs ],
                } # dữ liệu đang ở dạng dic
        df1 = pd.DataFrame(data) # convert về dạng pandas
        df1.index=df_numeric.keys() # keys sẽ trả về tên của các cột( features)
        data_complete = df1.transpose() # transpose để chuyển hàng về cột, cột về hàng

        # Thêm một cột mới vào đầu DataFrame
        new_column_data = ['count','min','max','median','mode','Q1','Q2','Q3','IQR','Variance','stdev']
        column_name = ' '
        data_complete.insert(loc=0, column=column_name, value=new_column_data)
        print(data_complete)
        data_complete.to_csv('Thong_ke_1.txt', sep='\t', index=False)

descriptive(data_count,column_min,column_max,column_medians,column_modes,column_q1,column_q2,column_q3,column_IQR,column_variances,column_std_devs)
print('---------------------------------------------------------------------------------------------------------------------------------------------')
# Tạo bảng thống kê (dùng hàm có sẵn)
data_complete = df_numeric.describe(include='all')
print(data_complete)
data_complete.to_csv('Thong_ke_2.txt', sep='\t', index=False)