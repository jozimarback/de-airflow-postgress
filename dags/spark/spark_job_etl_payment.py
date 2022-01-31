from pyspark.sql import SparkSession, functions as f
from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf()).getOrCreate()
# spark = SparkSession(sc).builder.config("spark.jars.packages","org.postgresql:postgresql:42.2.10").getOrCreate()
spark = SparkSession.builder.config("spark.jars.packages","org.checkerframework:checker-qual:3.5.0;com.github.waffle:waffle-jna:1.9.1;org.postgresql:postgresql:jar:42.2.4.jre7")\
    .config("spark.jars","postgresql-42.2.4.jar").getOrCreate()

df = spark.read.json("./dags/data/payments/0a13a9b3b19ecc9a9e48e2d30bb207ca.json")\
    .withColumn("paymentDate", f.to_timestamp("paymentDate"))\
    .withColumn("paymentValue", f.col("paymentValue").astype("double"))
# print(df.printSchema())
# print("done")
df.write.format("jdbc")\
    .option("url","jdbc:postgresql://172.17.0.1:5432/de_challenge")\
    .option("dbtable","public.payments")\
    .option("user", "postgres")\
    .option("password", "changeme")\
    .option("driver", "org.postgresql.Driver")\
    .mode("overwrite")\
    .save()

