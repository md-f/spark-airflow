"""
Daily extract top 3 page hits that lead to a user registering
"""
from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

SPARK_DATA = '/usr/local/airflow/spark'

default_args = {
    "owner": "marco",
    "depends_on_past": False,
    "start_date": days_ago(1),
    # "email": ["XXXX"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("test", default_args=default_args, schedule_interval=timedelta(1))

spark_submit_local = SparkSubmitOperator(application=f'{SPARK_DATA}/spark_example.py',
                                         conn_id='spark_local',
                                         task_id='example',
                                         dag=dag
                                         )

spark_submit_local
