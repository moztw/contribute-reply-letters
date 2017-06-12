from __future__ import print_function

import json
import boto3

ses = boto3.client('ses')

email_from = 'CHANGE_ME'
email_to = 'CHANGE_ME'
email_cc = ''
emaiL_subject = 'MozTW Volunteer test'
email_body = 'Hello '


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("name = " + event['name'])
    print("email = " + event['email'])
    # print("value3 = " + event['key3'])
    # return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
    print()
    send_email(event['email'], event['name'])


def send_email(email_to, name):
    response = ses.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            #'CcAddresses': [
            #    email_cc,
            #]
        },
        Message={
            'Subject': {
                'Data': emaiL_subject
            },
            'Body': {
                'Text': {
                    'Data': email_body + name
                }
            }
        }
    )
