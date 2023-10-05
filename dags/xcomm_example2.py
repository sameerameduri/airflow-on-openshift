from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'bmeduri',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(name, age):
    print(f"Hello World! My name is {name}, "
          f"and I am {age} years old!")

def get_name():
    return 'sameera'


with DAG(
    dag_id='python_operator_dag',
    default_args=default_args,
    description='This is a python operator dag',
    start_date=datetime(2023, 10, 5),
    schedule_interval='@daily'
) as dag:
    # task1 = PythonOperator(
    #     task_id='greet',
    #     python_callable=greet
    #     op_kwargs={'name':'sameera', 'age':'27'}
    # )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

    task2