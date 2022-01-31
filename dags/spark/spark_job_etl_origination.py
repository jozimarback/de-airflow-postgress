from pyspark.sql import SparkSession, functions as f
from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf()).getOrCreate()
spark = SparkSession(sc)

df = spark.read.json("./dags/data/originations/*.json")\
    .withColumn("registerDate", f.to_date(f.to_timestamp("registerDate")))\
    .withColumn("installmentId", f.explode(f.col("installments.installmentId")))\
    .withColumn("dueDate", f.explode(f.col("installments.dueDate")))\
    .withColumn("dueDate", f.to_date(f.to_timestamp("dueDate")))\
    .withColumn("installmentValue", f.explode(f.col("installments.installmentValue")))\
    .withColumn("installmentValue", f.col("installmentValue").astype("double"))

# print(df.printSchema())
# df.drop("installments").show()
# print("done")

df.select(
        "originationId"
        ,"clientId"
        ,"registerDate"
    ).write.jdbc(
    url="jdbc:postgresql://172.17.0.1:5432/de_challenge"
    ,table="originations"
    ,mode="overwrite"
    ,properties = {"user": "postgres","password": "changeme","driver": "org.postgresql.Driver"}
)

df.select(
        "originationId"
        ,"installmentId"
        ,"dueDate"
        ,"installmentValue"
    ).write.jdbc(
    url="jdbc:postgresql://172.17.0.1:5432/de_challenge"
    ,table="instalments"
    ,mode="overwrite"
    ,properties = {"user": "postgres","password": "changeme","driver": "org.postgresql.Driver"}
)