import os
import sys

from pyspark.sql.functions import col

sys.path.append(os.path.dirname(__file__) + '/common')
from common.spark_connectors import *

print("Start to get dataframe of tasks <= MongoDB")
df_tasks_src = mongo_dataframe("tasks")
df_tasks_src.printSchema()

df_tasks_src.show()
df_tasks_src \
    .filter(col("_id").getItem("oid").eqNullSafe('6091ae0f4da4b620cb21eddd')) \
    .show()

print("spark_jobs.py finished")
