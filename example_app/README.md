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
    3. airflow test dynamic_dag templated 2015-06-01 -tp '{"my_param":"~/path" }'
    4. airflow test dynamic_dag print_number 2015-06-01 -tp '{"n":"5" }'

#### References
    1. https://github.com/mikeghen/airflow-tutorial
    2. https://github.com/hgrif/airflow-tutorial
    3. https://gist.github.com/rosiehoyem/9e111067fe4373eb701daf9e7abcc423
