import yaml
from pyspark.sql import SparkSession
from sentence_transformers import SentenceTransformer


with open("../config/config.yml", "r") as f:
    config = yaml.safe_load(f)

spark = SparkSession.builder.getOrCreate()


def generate_embeddings(df_clean, model_name=None):
    if model_name is None:
        model_name = config["model"]["embedding_model"]

    print(f"Using embedding model: {model_name}")

    model = SentenceTransformer(model_name)

    df_embedded = df_clean.rdd.map(
        lambda row: (row.id, model.encode(row.processed_name).tolist(), row.category_id)
    ).toDF(["id", "embedding", "category_id"])

    return df_embedded
