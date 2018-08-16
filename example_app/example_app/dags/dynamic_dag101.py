import datetime as dt
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2018, 1, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


def create_dag(dag_id, schedule, dag_number, default_args):
    dag = DAG(dag_id, schedule_interval=schedule, catchup=False, default_args=default_args)

    def hello_world1(*args):
        print('hello_world1 DAG_ID:{} This is DAG: {}'.format(dag_id, str(dag_number)))

    def hello_world2(*args):
        print('hello_world2 DAG_ID:{} This is DAG: {} args:{}'.format(dag_id, str(dag_number), args))
    with dag:
        t1 = PythonOperator(task_id='hello_world1',python_callable=hello_world1)
        t2 = PythonOperator(task_id='hello_world2',python_callable=hello_world2)
    return dag


# build a dag for each number in range(10)
for n in range(1, 10):
    dag_id = 'dynamic_dag101_{}'.format(str(n))
    globals()[dag_id] = create_dag(dag_id, '@daily', n, default_args)