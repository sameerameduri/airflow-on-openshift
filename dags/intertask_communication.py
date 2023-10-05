import time

from datetime import datetime, timedelta
from airflow.utils.dates import days_ago

from airflow import DAG

from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'bmeduri'
}

def increment_by_1(value):
    print("Value {value}!".format(value=value))

    return value + 1

def multiply_by_100(ti):
    value = ti.xcom_pull(task_ids='increment_by_1')

    print("Value {value}!".format(value=value))

    return value * 100