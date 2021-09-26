
# conn_id='emr_spark',
# queue='emrspark',

spark-submit --jars /Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/com.google.protobuf_protobuf-java-3.6.1.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb.spark_mongo-spark-connector_2.12-3.0.1.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb_bson-4.0.5.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb_mongodb-driver-core-4.0.5.jar,/Users/lequoctruong/Documents/prog/turong/airflow-spark/common/jars/org.mongodb_mongodb-driver-sync-4.0.5.jar --master local --name push_task /Users/lequoctruong/Documents/prog/turong/airflow-spark/spark_jobs.py

spark-submit --master local --name push_task /Users/lequoctruong/Documents/prog/turong/airflow-spark/spark_jobs.py