from pyspark import SparkConf
from pyspark.sql import SparkSession

conf = SparkConf().set("spark.jars.packages",
                       "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1,mysql:mysql-connector-java:8.0.17")
spark_mongo = SparkSession \
    .builder \
    .master('local') \
    .appName("spark-mongo") \
    .config(conf=conf) \
    .getOrCreate()


def mongo_dataframe(coll):
    return spark_mongo.read \
        .format("com.mongodb.spark.sql.DefaultSource") \
        .option("spark.mongodb.input.uri", "mongodb://localhost:27017/todos." + coll) \
        .load()


spark_mysql = SparkSession \
    .builder \
    .appName('spark-mysql') \
    .master('local[*]') \
    .config("url", "jdbc:mysql://localhost/todos?useUnicode=true&serverTimezone=UTC") \
    .config("user", "root") \
    .config("password", "123456@A") \
    .getOrCreate()


def mysql_dataframe(table):
    return spark_mysql.read \
        .format("jdbc") \
        .option("url", "jdbc:mysql://localhost/todos?useUnicode=true&serverTimezone=UTC") \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("dbtable", table) \
        .option("user", "root") \
        .option("password", "123456@A") \
        .load()
