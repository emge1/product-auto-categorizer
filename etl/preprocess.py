from pyspark.sql.functions import col, lower, regexp_replace
import nltk
from nltk.corpus import stopwords


nltk.download("stopwords")
stopwords_list - stopwords.words("english")


def preprocess_text(df_spark, stopwords_list):
    df_clean = df_spark.withColumn("clean_name", lower(regexp_replace(col("name"), "[^a-zA-Z0-9]", "")))
    df_clean = df_clean.rdd.map(
        lambda row: (row.id, " ".join([word for word in row.clean_name.split() if word not in stopwords_list]))).toDF(
        ["id", "processed_name"])

    return df_clean
