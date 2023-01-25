from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
dag=DAG(dag_id="hello_task2", start_date=datetime(2022, 1, 1), schedule="0 0 * * *")

def hello_python():
    print("Hello Airflow!")

hello_python = PythonOperator(
    task_id='hello_python',
    python_callable=hello_python,
    dag=dag,
)