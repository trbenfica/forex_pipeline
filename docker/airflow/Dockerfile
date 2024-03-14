
from apache/airflow:2.8.1

run pip install apache-airflow-providers-apache-spark

env AIRFLOW_CONN_MY_PROD_DATABASE='{
    "conn_type": "Spark Connect",
    "host": "spark-master",
    "port": 8080,
}'

user root

run apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install openjdk-17-jdk -yqq
    
user airflow


