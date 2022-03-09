# if we install airflow, pyspark, gunicorn locally
export AIRFLOW_HOME=~/airflow

# initialize the database, remove airflow.db if reset
airflow db init

airflow users create \
--username admin \
--firstname Truong \
--lastname Le \
--role Admin \
--email lqtruong@gmail.com

# start the web server, default port is 8080
airflow webserver --port 8080

# start the scheduler
# open a new terminal or else run webserver with ``-D`` option to run it as a daemon
airflow scheduler

# start the first airflow task e.g. simple_operator.py
airflow dags trigger 'simple_operator' -r 'run_id' --conf '{"message":"value"}'