import os
import re
import unittest
from uuid import UUID

import boto3
from moto import mock_sqs

from notificationhub_sdk import Sms, Email, EmailRecipient, Platform, Whatsapp, Push, Task
# from notificationhub_sdk.common import MessageType


class TestNotificationTask(unittest.TestCase):
    def setUp(self) -> None:
        self.sms = Sms(send_to='8698009017', template='https://static.aasaanjobs.com/sms_template.html')

        self.email = Email(send_to=[EmailRecipient('john.doe@example.com', 'John Doe')],
                           template='https://static.aasaanjobs.com/email_template.html',
                           subject='Test Email', platform=Platform.Aasaanjobs)
        self.whatsapp = Whatsapp(send_to='8698009017', template='https://static.aasaanjobs.com/whatsapp_template.html')
        self.push = Push('cuhk5Noaw0M:APA91bGxjyUz4JDPj-AjmLIhNzDMxSMNcSGkMudnBvaWR_qhrEuc9mAHl6E4V5Gpo7mrTx0GjcsgvYVezTbzCMQhMEFD-WsXh3tlLJ4JdHwWDp9BSV8Fqf3Pks8GXQnsNNW3TZ_oF-ag',
                         'https://static.aasaanjobs.com/push_template.html')
        self.name = 'test_notification'
        self.sent_by_id = '1'
        self.client = 'api'
        self.platform = Platform.OLXPeople
        # self.message_type = MessageType.MARKETING

        """Mocked AWS Credentials for moto."""
        os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
        os.environ['AWS_SECURITY_TOKEN'] = 'testing'
        os.environ['AWS_SESSION_TOKEN'] = 'testing'
        os.environ['AWS_DEFAULT_REGION'] = 'ap-south-1'

        os.environ['NOTIFICATION_HUB_SQS_ACCESS_KEY_ID'] = 'testing'
        os.environ['NOTIFICATION_HUB_SQS_SECRET_ACCESS_KEY'] = 'testing'
        os.environ['NOTIFICATION_HUB_SQS_REGION'] = 'ap-south-1'
        os.environ['NOTIFICATION_HUB_SQS_QUEUE_NAME'] = 'hub-test'
        os.environ['NOTIFICATION_HUB_MARKETING_SQS_QUEUE_NAME'] = 'hub-test'

    def test_existence_of_channels(self):
        with self.assertRaises(AssertionError):
            Task(self.name, self.sent_by_id, self.client, self.platform)

    def test_sms(self):
        obj = Task(self.name, self.sent_by_id, self.client, self.platform, sms=self.sms)
        self.assertEqual(obj.proto.sms, self.sms.proto)

    def test_email(self):
        obj = Task(self.name, self.sent_by_id, self.client, self.platform, email=self.email)
        self.assertEqual(obj.proto.email, self.email.proto)

    def test_whatsapp(self):
        obj = Task(self.name, self.sent_by_id, self.client, self.platform, whatsapp=self.whatsapp)
        self.assertEqual(obj.proto.whatsapp, self.whatsapp.proto)

    def test_push(self):
        obj = Task(self.name, self.sent_by_id, self.client, self.platform, push=self.push)
        self.assertEqual(obj.proto.push, self.push.proto)

    def test_sqs_push(self):
        with mock_sqs():
            # Initialise a boto session
            sqs_session = boto3.client(service_name='sqs')
            # Create a test SQS queue
            res = sqs_session.create_queue(QueueName='hub-test')
            try:
                obj = Task(self.name, self.sent_by_id, self.client, self.platform, sms=self.sms)
                task_id, aws_id = obj.send()
                self.assertIsInstance(UUID(aws_id), UUID)
                sqs_session.delete_queue(QueueUrl=res['QueueUrl'])
            except Exception as ex:
                sqs_session.delete_queue(QueueUrl=res['QueueUrl'])
                raise ex
