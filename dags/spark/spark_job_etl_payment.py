from pyspark.sql import SparkSession, functions
from pyspark import SparkConf, SparkContext

sc = SparkContext(conf=SparkConf()).getOrCreate()
spark = SparkSession(sc)

json = spark.read.json("https://github.com/ScudraServicos/data-engineer-code-challenge/raw/main/payments.zip/payments")
json.printSchema()

