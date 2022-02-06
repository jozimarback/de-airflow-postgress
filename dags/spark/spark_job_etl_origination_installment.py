from pyspark.sql import SparkSession, functions as f
from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf().set("spark.jars.packages","org.postgresql:postgresql:42.2.10")).getOrCreate()
spark = SparkSession(sc)

df = (
    spark.read.json("../data/originations/*.json")
        .withColumn("registerDate", f.to_date(f.to_timestamp("registerDate")))
        .withColumn("installmentId", f.explode(f.col("installments.installmentId")))
        .withColumn("dueDate", f.explode(f.col("installments.dueDate")))
        .withColumn("dueDate", f.to_date(f.to_timestamp("dueDate")))
        .withColumn("installmentValue", f.explode(f.col("installments.installmentValue")))
        .withColumn("installmentValue", f.col("installmentValue").astype("double"))
)

df.select(
        "originationId"
        ,"clientId"
        ,"registerDate"
    ).distinct().write.option("truncate", "true").option("cascadeTruncate", "true").jdbc(
        url="jdbc:postgresql://host.docker.internal:5432/db_challenge"
        ,table="originations"
        ,mode="overwrite"
        ,properties={"user": "postgres","password": "changeme","driver": "org.postgresql.Driver"}
)

df.select(
        "originationId"
        ,"installmentId"
        ,"dueDate"
        ,"installmentValue"
    ).distinct().write.option("truncate", "true").option("cascadeTruncate", "true").jdbc(
        url="jdbc:postgresql://host.docker.internal:5432/db_challenge"
        ,table="instalments"
        ,mode="overwrite"
        ,properties={"user": "postgres","password": "changeme","driver": "org.postgresql.Driver"}
)