import os
import pymysql

host = os.environ['RDS_HOST_NAME']
user = os.environ['USER']
password = os.environ['PASS']
db = os.environ['DB']

connection = pymysql.connect(host=host, user=user, password=password, database=db)

def lambda_handler(event, context):
    with connection.cursor() as cursors:
        cursors.execute('show databases')
