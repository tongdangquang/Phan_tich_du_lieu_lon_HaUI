import pandas as pd
# DataFrame dùng để tạo bảng dữ liệu 2 chiều (2D) gồm hàng và cột
# tạo DataFrame từ dict
data = {
    "car": ["bmw", "volvo", "mercedes", "ford"],
    "passings": [3, 7, 2, 4],
    "value": [100, 200, 100, 400]
}
re1 = pd.DataFrame(data)
print(re1)

# tạo DataFrame từ list
data1 = [
    ['Alice', 25, 'Hà Nội'],
    ['Bob', 30, 'Đà Nẵng'],
    ['Charlie', 35, 'TP.HCM']
]

# thuộc tính columns dùng để đặt tên các cột, thuộc tính index dùng để thay thế chỉ số hàng, chỉ số mặt định sẽ bắt đầu từ 0
re2 = pd.DataFrame(data1, columns=["Tên", "Tuổi", "Thành phố"], index=[10, 11, 14])

print(re2['Tên']) # truy nhập cột

print(re2.loc[10]) # truy cập theo giá trị index bị thay đổi

print(re2.iloc[2]) # truy cập theo index, dù có thay đổi index thì chương trình vẫn trả về giá trị ở vị trí 2

print(re2.loc[10, 14, 11]) # trả về giá trị của các hàng tương ứng có chỉ số trong loc[]

re3 = re2.drop(columns=["Tuổi"]) # xóa cột
print(re3)
