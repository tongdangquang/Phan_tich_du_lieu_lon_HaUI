import pandas as pd
# 1. read_csv(): đọc file csv
df1 = pd.read_csv('chipotle.tsv', sep='\t', header=0, names=None, usecols=['order_id', 'item_price'], nrows=10, skiprows=None)
# sep: kí tự phân cách giữa các cột (mặc định là dấu phẩy ','). Nếu file .tsv thì có thể đẳt: sep = '\t'
# header: sô dọng chứa yên cột, mặt định là 0. Nếu file không có dòng tiêu đề, có thể đặt header = None
# names: danh sách tên cột. Nếu không sot tiêu đề trong file, bạn có thể cung cấp tên côt thông qua tham số này
# usecols: chọn các cột cụ thể cần đọc, ví dụ usecols=['Name', 'Age']: chỉ lấy ra cột Name và Age
# nrows: số dòng cần đọc từ file, ví dụ nrows = 10: chỉ đọc 10 dòng đầu
# skipprows: bỏ qua một số dòng đầu tiên của file khi đọc, ví dụ skiprows = 3: bỏ qua 3 dòng đầu tiên
print(df1)


# 2. read_json(): đọc file json
df2 = pd.read_json('data.json')
print(df2.head())


# 3. read_excel(): đọc file excel
pd.read_excel("filepath", sheet_name=0, header=0, usecols=None, nrows=None)
# filepath: Đường dẫn đến file Excel cần đọc.
# sheet_name: Tên của sheet cần đọc, hoặc chỉ số của sheet (bắt đầu từ 0).
# header: Số dòng chứa tên cột, mặc định là 0.
# usecols: Chọn các cột cụ thể cần đọc.
# nrows: Số dòng cần đọc từ đầu file.



