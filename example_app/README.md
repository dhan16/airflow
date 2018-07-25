# Airflow example app

### Run
    1. source setup_airflow_env.sh
    2. docker run -v $POSTGRES_HOME:/var/lib/postgresql/data -e POSTGRES_PASSWORD=airflow -p 5432:5432 -d postgres:10.3
    2. airflow initdb
    3. airflow webserver --port 8080
    4. go to localhost:8080

