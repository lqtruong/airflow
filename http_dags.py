import os
import sys
import time
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

sys.path.append(os.path.dirname(__file__))

app_configs = {
    'root_path': os.path.dirname(__file__)
}

args = {
    'owner': 'truong.le',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
    'provide_context': True
}

http_requests_jobs = app_configs['root_path'] + '/http_requests_jobs.py'

http_requests_jobs_configs = {
    'name': '{{ ti.task_id }}',
    'application': http_requests_jobs
}

with DAG(
        dag_id='http_requests_jobs_sample',
        default_args=args,
        schedule_interval='0/1 * * * *',  # schedule every 1 minute
        start_date=days_ago(2),
        dagrun_timeout=timedelta(minutes=60),
        tags=['http', 'test'],
        params={"day": time.time()},
        catchup=False
) as dag:
    http_call_test_job = SparkSubmitOperator(
        task_id='http_call_test',
        conn_id="local_spark_conn",
        queue='localspark',
        dag=dag,
        **http_requests_jobs_configs
    )

print_http_start_message = BashOperator(
    task_id='print_http_start_message',
    bash_command='echo "Start Http Call Task"',
)

print_http_end_message = BashOperator(
    task_id='print_http_end_message',
    bash_command='echo "End Http Call Task"',
)

print_http_start_message >> http_call_test_job >> print_http_end_message
