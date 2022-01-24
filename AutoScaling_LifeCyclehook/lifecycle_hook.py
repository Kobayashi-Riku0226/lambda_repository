import requests
import boto3
import time

ec2 = boto3.client('ec2')
autoscaling = boto3.client('autoscaling')

def lambda_handler(event, context):
    print(event['detail']['EC2InstanceId'])
    instanceid = event['detail']['EC2InstanceId']
    time.sleep(10)
    ec2_response = ec2.describe_instances(
        InstanceIds=[
        instanceid,
        ],
    )
    print(ec2_response['Reservations'][0]['Instances'][0]['PrivateIpAddress'])
    ipaddress = ec2_response['Reservations'][0]['Instances'][0]['PrivateIpAddress']
    for i in range(5):
        print(i)
        time.sleep(30)
        try:
            res = http_request(ipaddress)
            print(res)
            if res == 200:
                break
        except requests.exceptions.RequestException as e:
            print(e)

    print('Success')

    autoscaling_response = autoscaling.complete_lifecycle_action(
        LifecycleHookName=event['detail']['LifecycleHookName'],
        AutoScalingGroupName=event['detail']['AutoScalingGroupName'],
        LifecycleActionResult='CONTINUE',
        InstanceId=event['detail']['EC2InstanceId']
        )

def http_request(ipaddress):
    http_response = requests.get(url=f'http://{ipaddress}')
    print(http_response.status_code)
    return http_response.status_code