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


def foo(*args, **kwargs):
    dag_run_ = kwargs['dag_run']
    if dag_run_ is None:
        return False
    dag_run_params = dag_run_.conf
    n = dag_run_params.get('n')
    dag101_fns.print_number(n)
    return n


with DAG('dynamic_dag',
         default_args=default_args,
         catchup=False,
         schedule_interval=None,
         ) as dag:
    # this only works with trigger_dag
    python_paramed = PythonOperator(task_id='python_paramed',provide_context=True,python_callable=foo)

    # params.n  works with airflow test and dag_run.conf.n works with airflow trigger_dag
    templated_command = """
        {% for i in range(2) %}
            echo {{ ds }}
            echo {{ dag_run.conf.n if dag_run else params.n }}
        {% endfor %}
    """
    bash_templated = BashOperator(
        task_id='bash_templated',
        bash_command=templated_command,
        params={'n': 'default_n'},
        dag=dag)


python_paramed
bash_templated
