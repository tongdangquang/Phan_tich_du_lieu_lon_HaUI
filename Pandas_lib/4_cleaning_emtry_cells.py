import pandas as pd

# 1. xóa những ô trống
df = pd.read_csv('data.csv')
new_df = df.dropna() # dùng phương thức dropna() để trả về một DataFrame không chứa dữ liệu trống, phương thức dropna() sẽ không thay đổi dữ liệu gốc
new_df2 = df.dropna(inplace=True) # dùng dropna(inplace = True) nếu muốn thay đổi dữ liệu gốc

# 2. thay thế ô trống
df2 = pd.read_csv('data.csv')
new_df3 = df2.fillna(130) # thay thế các ô trống bằng 130, nhưng không làm thay đổi dữ liệu gốc
new_df4 = df2.fillna(130, inplace=True) # thay thế các ô trống bằng 130, dùng inplace=True sẽ làm thay đổi cả dữ liệu gốc
df2['Calories'].fillna(130, inplace=True) # thay thế giá trị cho cột chỉ định

# 3. thay thế bằng mean, median, mode(giá trị xuất hiện thường xuyên nhất)
# thế bằng mean (giá trị trung bình)
df3 = pd.read_csv('data.csv')
x = df3['Calories'].mean()
df3['Calories'].fillna(x, inplace=True)

# thay thế bằng median (trung vị: giá trị ở giữa, sau khi bạn đã sắp xếp tất cả các giá trị tăng dần)
x2 = df3['Calories'].median()
df3['Calories'].fillna(x2, inplace=True)

# thay thế bằng mode(giá trị xuất hiện thường xuyên nhất)
# giải thích 1 chút về hàm mode: hàm mode() sẽ lọc ra và trả về những giá trị xuất hiện nhiều nhất trong cột dữ liệu theo kiểu Series 
# Nếu có nhiều giá trị có cùng tần suất xuất hiện cao nhất, mode() sẽ giữ nguyên thứ tự của các giá trị như chúng xuất hiện trong dữ liệu gốc
# mode()[index] là chọn ra giá trị để thay thế vào cột dữ liệu
x3 = df3['Calories'].mode()
df3['Calories'].fillna(x3, inplace=True)




