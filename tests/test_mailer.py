import sys
from unittest.mock import Mock
sys.modules['boto3'] = Mock()
from src import mailer

def generate_no_interest_mail_body(name):
    with open('./emails/_header.txt', 'r') as f:
        header = f.read()
    with open('./emails/_footer.txt', 'r') as f:
        footer = f.read()
    content = header + "\n" +  footer
    content = content.replace('{%name%}', name)
    return content


def test_send_email():
    # ses = MockBoto3()
    to_email = "foo@bar.com"
    from_email = "community@mozilla.org" # TODO:?
    subject = "Welcome to Mozilla"
    name = "Foo Bar"

    content = "Hello Foo Bar"
    # content = generate_no_interest_mail_body(name)


    ses = Mock()
    mailer.send_email(ses, to_email, name)
    # ses.send_email.assert_called("foo")
    ses.send_email.assert_called_with(
        Destination = {'ToAddresses': [to_email]},
        Message={'Subject': {'Data': subject},
                 'Body': {'Text': {'Data': content}}},
        Source=from_email)

def test_format_body():
    name = "Foo Bar"
    interests = []
    content = generate_no_interest_mail_body(name)

    assert mailer.format_body(name, interests) == content

def test_content_variables():
    for key, val in mailer.contents.items():
        assert type(key) is str
        assert type(val) is str
        assert len(key) > 0
        assert len(val) > 0
