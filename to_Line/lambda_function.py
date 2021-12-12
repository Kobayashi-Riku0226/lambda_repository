import os
import requests
import json

token = os.environ['TOKEN_KEY']
url = os.environ['URL']
headers = {'Authorization':f'Bearer {token}'}

def lambda_handler(event, context):
    Message = json.loads(event['Records'][0]['Sns']['Message'])
    AlarmName = Message['AlarmName']
    NewStateValue = Message['NewStateValue']
    Instance = Message['Trigger']['Dimensions'][0]['value']
    NewStateReason = Message['NewStateReason']
    
    if NewStateValue == 'ALARM':
        data = {'message': f'\nアラーム名：{AlarmName}\
                \nステータス：{NewStateValue}\
                \nインスタンス：{Instance}\
                \n理由：{NewStateReason}',
                'stickerPackageId':789,
                'stickerId':10860}
        requests.post(url=url, data=data, headers=headers)
    elif NewStateValue == 'OK':
        data = {'message': f'\nアラーム名：{AlarmName}\
                \nステータス：{NewStateValue}\
                \nインスタンス：{Instance}\
                \n理由：{NewStateReason}',
                'stickerPackageId':789,
                'stickerId':10858}
        requests.post(url=url, data=data, headers=headers)