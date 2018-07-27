import datetime as dt
import os
import sys

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from example_app.dag_functions.dag101_fns import print_complex


def print_world():
    print('world')


def print_sys_path():
    print(sys.path)


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


with DAG('dag101',
         default_args=default_args,
         catchup=False,
         schedule_interval='0 * * * *',
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    print_world = PythonOperator(task_id='print_world',
                                 python_callable=print_world)
    print_sys_path = PythonOperator(task_id='print_sys_path',
                                    python_callable=print_sys_path)
    print_complex = PythonOperator(task_id='print_complex',
                                       python_callable=print_complex)


print_hello >> sleep >> print_world >> print_sys_path >> print_complex
