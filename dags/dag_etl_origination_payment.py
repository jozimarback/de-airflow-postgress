from airflow import DAG

from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

from io import BytesIO
from zipfile import ZipFile
from datetime import datetime, timedelta
from urllib.request import urlopen

default_args = {
    'owner': 'jozimar',
    'depends_on_past': False,
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def unzipfile(path_to_zip_file:str, directory_to_extract_to:str):
    """
        Unzip files
    """
    resp = urlopen(path_to_zip_file)
    with ZipFile(BytesIO(resp.read())) as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

with DAG(
    'dag_etl_origination_payment_v1_0_0',start_date=datetime(2022,1,28), default_args=default_args, schedule_interval=None
) as dag:
    task_start = DummyOperator(
        task_id='start'
    )

    task_unzip_payments = PythonOperator(
        task_id='unzip_payments',
        python_callable=unzipfile,
        op_kwargs={
            "path_to_zip_file":"https://github.com/ScudraServicos/data-engineer-code-challenge/raw/main/payments.zip",
            "directory_to_extract_to":"./dags/data/"
        }
    )

    task_unzip_origination = PythonOperator(
        task_id='unzip_origination',
        python_callable=unzipfile,
        op_kwargs={
            "path_to_zip_file":"https://github.com/ScudraServicos/data-engineer-code-challenge/raw/main/originations.zip",
            "directory_to_extract_to":"./dags/data/"
        }
    )

    task_start >> [task_unzip_payments, task_unzip_origination]
