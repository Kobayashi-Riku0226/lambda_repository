from datetime import datetime
import boto3
import os

ssm = boto3.client('ssm')

instance_id = os.environ['instance_id']
now = datetime.now()
file_name = 'file_name' + now.strftime('%Y%m%d%H%M%S')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName='AWS-RunShellScript',
        Parameters={
            'commands': [
                f'aws s3 cp s3://{bucket}/{key} /home/ec2-user/{file_name}'
            ],
            'executionTimeout': ['3600']
        }
    )
