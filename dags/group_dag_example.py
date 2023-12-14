from airflow.decorators import task_group
from airflow.operators.bash import BashOperator
from airflow.operators.bash import EmptyOperator
from airflow import DAG

default_args = {
    'owner': 'bmeduri',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}

@task_group()
def group1():
     task1 = BashOperator(task_id="first_task")
     task2 = BashOperator(task_id="second_task")

task3 = EmptyOperator(task_id="task3")

group1() >> task3


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





