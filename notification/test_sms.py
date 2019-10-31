import unittest
from notification.sms import Sms
from notification.common import Waterfall
from notification.task import Task
from notification.sqs_config import SqsConfig


class TestSms(unittest.TestCase):

    def test_Sms(self):
        sms_obj = Sms()

        sms_template = "sms_template"
        sms_obj.set_template(sms_template)
        self.assertEqual(sms_obj.get_template(), sms_template)

        mobile = "1234567890"
        sms_obj.set_mobile(mobile)
        self.assertEqual(sms_obj.get_mobile(), mobile)

        sms_context = "sms_context"
        sms_obj.set_context(sms_context)
        self.assertEqual(sms_obj.get_context(), sms_context)

        sms_obj.set_waterfall_config(Waterfall(1, 20))

        sqs_config = SqsConfig("AKIAJO4MSDD6WYU4AQRA", "AHOVq4t+C6zyUbIuIMDcVGKNeCsK50+6cD0NNZ+u",
                               "https://ap-south-1.queue.amazonaws.com/856777734734/notification-hub-dev", "ap-south-1")
        task_obj = Task(sqs_config=sqs_config)
        task_obj.set_sms(sms_obj)
        self.assertNotEqual(task_obj.get_sms(), None)
