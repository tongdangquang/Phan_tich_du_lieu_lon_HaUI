from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder \
    .appName("DistributedQueryExample") \
    .getOrCreate()

# # Đọc dữ liệu từ file CSV và tạo DataFrame
df = spark.read.csv("data/orders_spark.csv", header=True, inferSchema=True)
dic = {}
kq = df.select(max('amount').alias('max'),
               min('amount').alias('min'),
               std('amount').alias('std'),
               variance('amount').alias('var'),
               percentile_approx('amount', 0.25, 10000000).alias('Q1'),
               percentile_approx('amount', 0.5).alias('Q2'),
               percentile_approx('amount', 0.75).alias('Q3'))
kq.show()
a = [kq.first()['max'], kq.first()['min'], kq.first()['std'],
     kq.first()['var'], kq.first()['Q1'],  kq.first()['Q2'],  kq.first()['Q3']]
dic['amount'] = a
print(a)
print(dic)
spark.stop()