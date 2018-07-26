export POSTGRES_HOME="$(pwd)"/runtime/postgres
export AIRFLOW_HOME="$(pwd)"/runtime/airflow_home
mkdir -p $POSTGRES_HOME 
mkdir -p $AIRFLOW_HOME 

export AIRFLOW__CORE__LOAD_EXAMPLES="False"
export AIRFLOW__CORE__EXECUTOR="LocalExecutor"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql+psycopg2://postgres:passw0rd@localhost:5432/postgres"
