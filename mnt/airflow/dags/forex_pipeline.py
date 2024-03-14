from airflow import DAG
from datetime import datetime, timedelta, date
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from scripts.download_forex import download_forex
from scripts.load_data_to_postgres import load_data_to_postgres

default_args = {
  "owner": "airflow",
  "email_on_failure": False,
  "retries": 1,
  "retry_delay": timedelta(minutes=5)
}


with DAG("FOREX", start_date=datetime(2024, 1, 27), schedule_interval='0 12 * * 1-5', 
    default_args=default_args, catchup=False) as dag:
  
  # (Extract) - Extrai dados da API
  extract_data = PythonOperator(
          task_id="extract_data",
          python_callable=download_forex
  )

  # (Transform) - Processa os dados num dataframe
  process_data = SparkSubmitOperator(
          task_id="process_data",
          application="/opt/airflow/dags/scripts/process_data.py",
          conn_id="spark_default",
          verbose=False
  )

  # (Load) carrega os dados para o destino
  load_data = PythonOperator(
          task_id="load_data",
          python_callable=load_data_to_postgres
  )

  extract_data >> process_data >> load_data
          
