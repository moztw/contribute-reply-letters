import json
import boto3

ses = boto3.client('ses')

def lambda_handler(event, context):
    {% macro include_indented() %}{% include "global_config.py" %}{% endmacro %}
    {{ include_indented()|indent }}

    #print("Received event: " + json.dumps(event, indent=2))
    print("name = " + event['name'])
    print("email = " + event['email'])
    print("interests = " + str(event['interests']))
    # print("value3 = " + event['key3'])
    # return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
    send_email(ses,
               email_from,
               event['email'],
               email_cc,
               email_subject,
               format_body(event['name'], event['interests']))


def send_email(ses_service, email_from, email_to, email_cc, subject, body):
    response = ses_service.send_email(
        Source = email_from,
        Destination={
            'ToAddresses': [
                email_to,
            ],
            'CcAddresses': [
                email_cc,
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
