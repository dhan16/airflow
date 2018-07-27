import datetime as dt
import os
import sys

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from example_app.dag_functions import dag101_fns


default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 6, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}


def foo(templates_dict, *args, **kwargs):
    print(templates_dict)
    dag101_fns.print_number(templates_dict['n'])
    return templates_dict['n']


with DAG('dynamic_dag',
         default_args=default_args,
         catchup=False,
         schedule_interval=None,
         ) as dag:

    print_hello = BashOperator(task_id='print_hello',
                               bash_command='echo "hello"')
    sleep = BashOperator(task_id='sleep',
                         bash_command='sleep 5')
    print_number = PythonOperator(task_id='print_number',
                                  provide_context=True,
                                  templates_dict={'n': '{{ n }}'},
                                  # params={'n': 0},
                                  python_callable=foo)

    templated_command = """
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7)}}"
            echo "{{ params.my_param }}"
        {% endfor %}
    """

    t3 = BashOperator(
        task_id='templated',
        bash_command=templated_command,
        params={'my_param': 'Parameter I passed in'},
        dag=dag)


print_hello >> sleep >> print_number
t3
