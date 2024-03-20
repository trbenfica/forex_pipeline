
FROM apache/airflow:2.8.1

COPY postgresql-42.7.3.jar /driver/

RUN pip install apache-airflow-providers-apache-spark && \
    pip install PyYAML

ENV AIRFLOW_CONN_SPARK_DEFAULT='{"conn_type": "Spark Connect", "host": "spark-master", "port": 8080}' \
    CLASSPATH=/driver

USER root

RUN apt-get update -y && \
   apt-get upgrade -yqq && \
   apt-get install openjdk-17-jdk -yqq
    
USER airflow


