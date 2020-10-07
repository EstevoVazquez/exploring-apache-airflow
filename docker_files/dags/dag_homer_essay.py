
from datetime import datetime
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'homer_j_simpsom',
    'start_date': datetime(2020, 5, 20, 11, 0, 0)
}

def write_title():
    print("El uso de Airflow en la universidad de Springfield.")

def write_intro():
    print("El otro día mi hija me dijo que Airflow no se utilizaba en la universidad de Springfield, y yo le dije: qué no Lisa? qué no?")

def write_body():
    for i in range(50):
        print("Púdrete Flanders")


with DAG('dag_homer_essay',
         default_args=default_args,
         schedule_interval='@daily') as dag:
    
    start = DummyOperator(task_id='start')
    wr_title = PythonOperator(task_id='wr_title',python_callable=write_title)
    wr_intro = PythonOperator(task_id='wr_intro',python_callable=write_intro)
    wr_body = PythonOperator(task_id='wr_body',python_callable=write_body)
    end = DummyOperator(task_id='end')

start >> wr_title >> wr_intro >> wr_body >> end