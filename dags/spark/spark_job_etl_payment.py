from pyspark.sql import SparkSession, functions as f
from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf().set("spark.jars.packages","org.postgresql:postgresql:42.2.10")).getOrCreate()
spark = SparkSession(sc)

df = (spark.read.json("../data/payments/*.json")
    .withColumn("paymentDate", f.to_timestamp("paymentDate"))
    .withColumn("paymentValue", f.col("paymentValue").astype("double")))

df.write.jdbc(url="jdbc:postgresql://host.docker.internal:5432/db_challenge"
        ,table="payments"
        ,properties={
            "user": "postgres",
            "password": "changeme",
            "driver": "org.postgresql.Driver"
    }
    ,mode="overwrite")
