from airflow.models import Variable

print("http_requests_jobs.py started")

try:
    http_host = Variable.get("http_host")
    print("http_host:", http_host)
except Exception as e:
    print("error when getting variable: ", "http_host")
    print(e)

print("http_requests_jobs.py finished")
