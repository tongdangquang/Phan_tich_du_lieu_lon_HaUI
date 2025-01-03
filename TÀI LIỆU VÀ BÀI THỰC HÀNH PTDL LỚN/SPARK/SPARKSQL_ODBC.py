import pyodbc
import pandas as pd
from pyspark.sql import SparkSession


# Tạo Spark session
spark = SparkSession.builder \
    .appName("PySpark SQL Server ODBC Example") \
    .getOrCreate()

# Kết nối đến SQL Server bằng ODBC
connection_string  = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=RICKY;"
    "DATABASE=ECGM;"
    "UID=sa;"
    "PWD=123456;"
    #Nếu không đặt user name và password cho db, sử dụng Trusted connection
    #"Trusted_Connection=yes;"
)

conn = pyodbc.connect(connection_string)


query = "SELECT id, name, address FROM patient"

# Sử dụng pandas để tải dữ liệu từ SQL Server
pandas_df = pd.read_sql(query, conn)

print(pandas_df.to_string())
spark.stop()
