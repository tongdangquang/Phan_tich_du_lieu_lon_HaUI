#Ví dụ về suwr dụng Spark SQL truy vấn trên json
from pyspark.sql import SparkSession

# Khởi tạo một phiên Spark
spark = SparkSession.builder \
    .appName("Spark SQL JSON Example") \
    .getOrCreate()

# Đọc dữ liệu JSON vào DataFrame
df = spark.read.json("data/test.json")

# Đăng ký DataFrame làm bảng tạm thời
df.createOrReplaceTempView("people")

# Viết câu truy vấn SQL
sql_query = 'SELECT * FROM people WHERE age > 30'

# Thực thi truy vấn SQL
results = spark.sql(sql_query)

# Hiển thị kết quả
results.show()

# Đóng phiên Spark
spark.stop()