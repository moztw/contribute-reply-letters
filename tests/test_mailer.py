import sys
from unittest.mock import Mock
sys.modules['boto3'] = Mock()
from src import mailer

class MockBoto3():
    def send_email(Source, Destination, Message):
        print("Source")
        assert Source == "bar"

def test_send_email():
    # ses = MockBoto3()
    to_email = "foo@bar.com"
    from_email = "community@mozilla.org" # TODO:?
    subject = "Welcome to Mozilla"
    name = "Foo Bar"
    content = "Hello Foo Bar"

    ses = Mock()
    mailer.send_email(ses, to_email, name)
    # ses.send_email.assert_called("foo")
    ses.send_email.assert_called_with(
        Destination = {'ToAddresses': [to_email]},
        Message={'Subject': {'Data': subject},
                 'Body': {'Text': {'Data': content}}},
        Source=from_email)
