# spark-airflow
Airflow and Spark on the same Docker container

### Initialization: 
Build the docker image with
    
    docker build -t spark-airflow .
    
Run the containers with docker-compose:
    
    docker-compose up -d

Add an airflow connection to run airflow SparkSubmitOperator locally:

    docker exec -it spark-airflow /entrypoint.sh airflow connections -a --conn_id spark_local --conn_host local --conn_type spark

### Misc
Airflow available at http://localhost:8080/admin/
Spark UI available at http://localhost:4040 (but first you need to run pyspark inside the container)

### Credits
Thanks to puckel for the airflow docker project (https://github.com/puckel/docker-airflow)