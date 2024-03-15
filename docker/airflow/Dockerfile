
FROM apache/airflow:2.8.1

RUN pip install apache-airflow-providers-apache-spark

ENV AIRFLOW_CONN_SPARK_DEFAULT='{"conn_type": "Spark Connect", "host": "spark-master", "port": 8080}'

USER root

RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install openjdk-17-jdk -yqq
    
USER airflow


