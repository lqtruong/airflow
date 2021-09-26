from pyspark.sql.functions import col

from spark_connectors import *

print("Hello World! Connect to MongoDB")

df_tasks_src = mongo_dataframe("tasks")
df_tasks_src.printSchema()

df_tasks_src.show()
df_tasks_src \
    .filter(col("_id").getItem("oid").eqNullSafe('6091ae0f4da4b620cb21eddd')) \
    .show()

print("Connect to MySQL")

df_task_target = mysql_dataframe("task")
df_task_target.printSchema()

df_task_target.show()

print("Task has id > 2")
df_task_target.filter(df_task_target['id'] > 2).show()
df_task_target.select("name").show()

columns = ['id', 'name', 'desc', 'person_id', 'created_at', 'updated_at', 'm_id']
vals = []
for t in df_tasks_src.rdd.collect():
    vals.append((0, t['name'], t['desc'], t['person']['_id']['oid'], t['createdAt'], t['updatedAt'], t['_id']['oid']))

print("Save to MySQL task table from MongoDB")
newRow = spark_mysql.createDataFrame(vals, columns)
newRow.show()
appended = df_task_target.union(newRow)
appended.show()

appended.write \
    .format("jdbc") \
    .mode('append') \
    .option("url", "jdbc:mysql://localhost/todos?useUnicode=true&serverTimezone=UTC") \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("dbtable", 'task') \
    .option("user", "root") \
    .option("password", "123456@A") \
    .save()

spark_mysql.stop()  # closing the spark session
