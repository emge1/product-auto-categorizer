# Overview 
This project aims to automate product classification using PySpark for ETL, PostgreSQL for storage, and PyTorch for 
AI-driven categorization.

# Table of contents
* [Functionalities](#functionalities)
* [Project setup](#project-setup)
*  [Dependencies](#dependencies)

# Functionalities
* Connection with PostgreSQL via PySpark
* Pylint for static analysis of the code
* Data preprocessing using NLTK

# Project setup

Clone the repository:
```bash
git clone https://github.com/emge1/product-auto-categorizer.git
cd product-auto-categorizer
```
Create .env file:
```bash
cat <<EOT > .env
DB_HOST=localhost
DB_USER=postgres_user
DB_PASSWORD=postgres_password
DB_NAME=postgres_db
DB_PORT=5433
SPARK_JAR_PATH=<your-path-to-postgresql-42.7.5.jar>
EOT
```
Set up a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate.bat
```
Install dependencies:
```bash
pip install -r requirements.txt 
```

# Dependencies
* psycopg2==2.9.10
* sqlalchemy==2.0.38
* pandas==2.2.3
* torch==2.6.0
* python-decouple==3.8
* pyspark==3.5.4
* pylint==3.3.4

## Database
PostgreSQL 17

## PostgreSQL JDBC Driver
postgresql-42.7.5.jar
