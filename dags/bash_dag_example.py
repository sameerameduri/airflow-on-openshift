from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'bmeduri',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}

with DAG(
    dag_id='first_bash_dag_v2',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2023, 10, 5),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task!"
    )
    

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hello world, this is the second task and will run after first"
    )

    task1.set_downstream(task2)