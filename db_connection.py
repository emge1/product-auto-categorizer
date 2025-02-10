import decouple
from pyspark.sql import SparkSession


DB_HOST = decouple.config("DB_HOST")
DB_PORT = decouple.config("DB_PORT")
DB_NAME = decouple.config("DB_NAME")
DB_USER = decouple.config("DB_USER")
DB_PASSWORD = decouple.config("DB_PASSWORD")
SPARK_JAR_PATH = decouple.config("SPARK_JAR_PATH")

spark = SparkSession.builder. \
    appName("ETL_Product_Processing") \
    .config("spark.driver.memory", "2g") \
    .config("spark.jars", SPARK_JAR_PATH) \
    .getOrCreate()

df_spark = spark.read \
    .format("jdbc") \
    .option("url", f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}") \
    .option("dbtable", "products_product") \
    .option("user", DB_USER) \
    .option("password", DB_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

df_spark.show(5)



