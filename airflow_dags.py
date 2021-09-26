import os
import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.dates import days_ago

sys.path.append(os.path.dirname(__file__))

app_configs = {
    'root_path': '/Users/lequoctruong/Documents/prog/turong/airflow-spark/'
}

args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 9, 25),
    'retries': 1,
    'retry_delay': timedelta(minutes=30),
    'provide_context': True
}

spark_jobs_app = app_configs['root_path'] + 'spark_jobs.py'

spark_jobs_configs = {
    'name': '{{ ti.task_id }}',
    'application': spark_jobs_app,
    'packages': 'org.mongodb.spark:mongo-spark-connector_2.12:3.0.1,mysql:mysql-connector-java:8.0.17',
    # 'jars': '/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/com.google.protobuf_protobuf-java-3.6.1.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb.spark_mongo-spark-connector_2.12-3.0.1.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb_bson-4.0.5.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb_mongodb-driver-core-4.0.5.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb_mongodb-driver-sync-4.0.5.jar'
}

with DAG(
        dag_id='depends_multiple_tasks',
        default_args=args,
        schedule_interval='0/1 * * * *',  # schedule every 1 minute
        start_date=days_ago(2),
        dagrun_timeout=timedelta(minutes=60),
        tags=['example', 'example2'],
        params={"example_key": "example_value"},
        catchup=False
) as dag:
    # my_name = 'Truong'
    print_name = BashOperator(
        task_id='print_name',
        bash_command='echo "Truong"',
    )

    # my_age = 5
    print_age = BashOperator(
        task_id='print_age',
        bash_command='echo "5"',
    )

    # my_address = 'Go vap'
    print_address = BashOperator(
        task_id='print_address',
        bash_command='echo "Go vap"',
    )

    push_task = SparkSubmitOperator(
        task_id='push_task',
        conn_id='a_local_spark',
        queue='localspark',
        dag=dag,
        **spark_jobs_configs
    )

# end_message = 'Good Bye'
print_end_message = BashOperator(
    task_id='print_end_message',
    bash_command='echo "Good Bye"',
)

tasks = [
    print_name,
    print_age,
    print_address
]

tasks >> push_task >> print_end_message
