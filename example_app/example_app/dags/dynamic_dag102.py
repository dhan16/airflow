import datetime as dt
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 1, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


def create_dag(dag_id, schedule, default_args):
    dag = DAG(dag_id, schedule_interval=schedule, catchup=False, default_args=default_args)

    def hello_world(*args):
        print('hello_world DAG_ID:{}'.format(dag_id))
    with dag:
        t1 = PythonOperator(task_id='hello_world',python_callable=hello_world)
    return dag


context_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dynamic_dags_context')
files = os.listdir(context_dir)
# build a dag for each file in files
for f in files:
    dag_id = 'dynamic_dag102_{}'.format(f)
    globals()[dag_id] = create_dag(dag_id, '@daily',default_args)