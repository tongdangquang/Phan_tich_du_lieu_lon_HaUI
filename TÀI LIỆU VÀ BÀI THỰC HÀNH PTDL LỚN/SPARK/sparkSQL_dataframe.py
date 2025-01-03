#Ví dụ về sử dụng Spark SQL truy vấn trên data frame (file .csv)
from pyspark.sql import SparkSession

# Khởi tạo một SparkSession
spark = SparkSession.builder \
    .appName("DistributedQueryExample") \
    .getOrCreate()

# Đọc dữ liệu từ file CSV và tạo DataFrame
# header = True tức là dữ liệu có nhãn và header = False là dữ liệu không có nhãn
# inferSchema = True để tự động phát hiện kiểu dữ liệu phù hợp cho từng cột dữ liệu
df = spark.read.csv("orders_spark.csv", header=True, inferSchema=True)

# Đăng ký DataFrame như một bảng tạm thời để sử dụng với Spark SQL
df.createOrReplaceTempView("orders")

# Thực hiện truy vấn SQL phân tán
# SQL đơn giản: SELECT FROM WHERE
result1 = spark.sql("SELECT * FROM orders where amount = (select max(amount) from orders)")

result2 = df.filter("amount > 120").select("id", "orderid", "amount") # truy vấn bằng LINQ
# filter ngang với where
# chuyển từ câu lệnh LINQ sang SQL server
# SELECT id, orderid, amount
# FROM df
# WHELE amount > 120

result3 = df.filter("amount < 500").select("id", "orderid", "amount").orderBy(df['amount'].desc())
# trường hợp có AND ở điều kiện WHERE
result6 = df.filter("amount < 500 and amount > 200").select("id", "orderid", "amount").orderBy(df['amount'].desc())

result4 = df.filter("amount>100").select("id", "orderid", "amount").groupby("id", "orderid").agg({'amount':"sum"})

result5 = result2.join(result3, on='id', how='inner')

# # Hiển thị kết quả
# tham số n cho biết muốn lấy bap nhiêu dữ liệu (ví dụ n = 1 là muốn lấy 1 cái đầu tiên)
# result1.show(n=result1.count()) #show hết
result2.show(n=result2.count())
result3.show(n=result3.count())
# result4.show(n=result4.count())
result5.show(n=result5.count())

# Đóng SparkSession để tiết kiệm tài nguyên
spark.stop()