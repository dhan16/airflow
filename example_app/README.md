# Airflow example app

### Run
    1. source setup_airflow_env.sh
    2. docker run --name airflow_postgres -v $POSTGRES_HOME:/var/lib/postgresql/data -e POSTGRES_PASSWORD=passw0rd -p 5432:5432 -d postgres:10.3
    3. airflow initdb
    4. airflow scheduler
    5. airflow webserver --port 8080
    6. go to localhost:8080

### Test 
    * airflow list_tasks dag101 --tree
    * airflow test dag101 print_complex 2015-06-01
    * airflow test triggered_dag101 bash_templated 2015-06-01 -tp '{"n":1 }'

### Trigger DAG dynamically
    * airflow trigger_dag triggered_dag101 -c '{"n":2 }' -e 2018-07-31T09:21:22

### Get state
    * airflow dag_state triggered_dag101 2018-07-31T09:21:22
    * airflow task_state triggered_dag101 bash_templated 2018-07-31T09:21:22

#### References
    1. https://github.com/mikeghen/airflow-tutorial
    2. https://github.com/hgrif/airflow-tutorial
    3. https://github.com/astronomerio/airflow-guides/blob/master/guides/dynamically-generating-dags.md
    4. https://github.com/trbs/airflow-examples/blob/master/dags/example_python_operator.py
