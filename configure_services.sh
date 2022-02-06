#docker exec -it de-code-challenge_airflow-worker_1 echo "airflow:airflow" | chpasswd && adduser airflow sudo 
docker exec -it de-code-challenge_airflow-scheduler_1 pip install apache-airflow[apache.spark]
docker exec -it de-code-challenge_airflow-worker_1 sudo apt update
docker exec -it de-code-challenge_airflow-worker_1 sudo apt install default-jdk
docker exec -it de-code-challenge_airflow-worker_1 export JAVA_HOME='/usr/lib/jvm/java-8-openjdk-amd64' >> ~/.bashrc
docker exec -it de-code-challenge_airflow-worker_1 export PATH=$PATH:$JAVA_HOME/bin >> ~/.bashrc
docker exec -it de-code-challenge_airflow-worker_1 mkdir -p /opt/spark/
docker exec -it de-code-challenge_airflow-worker_1 wget -qO- https://dlcdn.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz | tar xvz - -C /opt/spark/
docker exec -it de-code-challenge_airflow-worker_1 export SPARK_HOME='/opt/spark'  >> ~/.bashrc
docker exec -it de-code-challenge_airflow-worker_1 export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin  >> ~/.bashrc
docker exec -it de-code-challenge_airflow-worker_1 pip install pyspark==3.2.0

docker exec -it de-code-challenge_airflow-worker_1 pip install apache-airflow-providers-apache-spark==2.0.2