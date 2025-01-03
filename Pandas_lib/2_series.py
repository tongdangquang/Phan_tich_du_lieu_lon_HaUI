import pandas as pd
# Series được hiểu như một côt trong bảng (thực chất nó là mảng một chiều chứa dữ liệu thuộc bất kỳ loại nào) và chỉ gầm duy nhất 2 cột index và value
# khởi tạo Series
data = {
    "car": ["bmw", "volvo", "mercedes", "ford"],
    "passings": [3, 7, 2, 4],
    "value": [100, 200, 100, 400]
}
data3 = ["Nguyễn Văn A", "Nguyễn Văn B", "Nguyễn Văn C"]

re3 = pd.Series(data3, index=[10, 11, 12]) # khởi tạo Series từ list

re4 = pd.Series(data) # khởi tạo Series từ dict, các key của dict sẽ trở thành index và các value sẽ trở thành giá trị tương ứng trong Series

re5 = pd.Series(5, index=['a', 'b', 'c', 'd']) # khởi tạo Series từ một giá trị vô hướng

# truy cập Series theo chỉ mục tương ứng
print(re3[10]) # cách 1: truy cập theo index đã được thay đổi

print(re3.iloc[0]) # cách 2: truy cập theo index, dù có thay đổi index thì chương trình vẫn trả về giá trị ở vị trí 2

# thao tác với Series (cộng, trừ, nhân, chia giá trị)
re5 = re5 * 5
re5 -= 10
re3 += " Hello world" # cũng có thể cộng chuỗi

# kiểm tra sẽ giá trị có null hay không
re6 = pd.Series([1, 2, None, "Hello", 5])
check_null = re6.isna() # trả về True nếu giá trị là NaN
re6 = re6.fillna(0) # thay thế giá trị NaN bằng 0

# Mối liên kết giữa Series và DataFrame là: Series chỉ có duy nhất 1 hàng, 1 cột trong khi đó DataFrame không giới hạn số hàng và cột,
# vì vậy mà có thể hiểu Series chính là một cột trong DataFrame và hoàn toàn có thể chuyển Series thành DataFrame
dt = [10, 20, 30]
idx = ['a', 'b', 'c']
s = pd.Series(dt, index=idx)
df = s.to_frame(name="Giá trị") # chuyển Series thành DataFrame với hàm to_frame và thuộc tính name= để đặt tên cột giá trị

# dùng vòng lặp để in giá trị cũng khá OK
for i in re3:
    print(i)