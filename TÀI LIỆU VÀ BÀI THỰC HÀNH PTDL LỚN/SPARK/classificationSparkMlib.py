from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("DecisionTreeClassifierExample") \
    .getOrCreate()

df = spark.read.csv("iris_full.csv", header=True, inferSchema=True)

# Xây dựng VectorAssembler để tạo vectơ đặc trưng từ các cột đầu vào
vector_assembler = VectorAssembler(inputCols=["A", "B", "C", "D"], outputCol="features")
df_vector = vector_assembler.transform(df)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
train_data, test_data = df_vector.randomSplit([0.7, 0.3], seed=123)

print(train_data.head())
# Khởi tạo mô hình Decision Tree Classifier
dt = DecisionTreeClassifier(labelCol="CLASS", featuresCol="features")
# Huấn luyện mô hình trên tập huấn luyện
dt_model = dt.fit(train_data)

predictions = dt_model.transform(test_data)

# Hiển thị kết quả dự đoán
predictions.select("features", "CLASS", "prediction").show()

# Đánh giá hiệu suất của mô hình
evaluator = MulticlassClassificationEvaluator(labelCol="CLASS", predictionCol="prediction", metricName="weightedRecall")
accuracy = evaluator.evaluate(predictions)
print("Accuracy on test data = %g" % accuracy)

# Đóng SparkSession
spark.stop()