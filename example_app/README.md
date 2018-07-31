# Airflow example app

### Run
    1. source setup_airflow_env.sh
    2. docker run --name airflow_postgres -v $POSTGRES_HOME:/var/lib/postgresql/data -e POSTGRES_PASSWORD=passw0rd -p 5432:5432 -d postgres:10.3
    3. airflow initdb
    4. airflow scheduler
    5. airflow webserver --port 8080
    6. go to localhost:8080

### Test 
    1. airflow list_tasks dag101 --tree
    2. airflow test dag101 print_complex 2015-06-01
    3. airflow test dynamic_dag bash_templated 2015-06-01 -tp '{"n":1 }'

### Trigger DAG dynamically
    1. airflow trigger_dag dynamic_dag -c '{"n":2 }' -e 2018-07-31T09:21:22
    2. airflow dag_state dynamic_dag 2018-07-31T09:21:22
    3. airflow task_state dynamic_dag bash_templated 2018-07-31T09:21:22

#### References
    1. https://github.com/mikeghen/airflow-tutorial
    2. https://github.com/hgrif/airflow-tutorial
