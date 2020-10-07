import pandas as pd
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils import dates
from airflow.hooks.postgres_hook import PostgresHook

default_args = {
    'owner': 'estevo_vazquez',
    'start_date': dates.days_ago(1)
}


def obtener_pandas():
    conn = PostgresHook('pg_local')
    df = conn.get_pandas_df('select * from emp')
    print (df)

with DAG('dag_leer_posgres',
default_args=default_args,
         schedule_interval='@daily') as dag:

    start = DummyOperator(task_id='start')
    obtener_pandas_operator = PythonOperator(task_id='obtener_pandas_operator',python_callable=obtener_pandas)
    end = DummyOperator(task_id='end')

start >> obtener_pandas_operator >> end