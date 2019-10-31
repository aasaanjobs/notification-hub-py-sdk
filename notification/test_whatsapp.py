import unittest
from notification.whatsapp import Whatsapp
from notification.common import Waterfall
from notification.task import Task
from notification.sqs_config import SqsConfig


class TestWhatsapp(unittest.TestCase):

    def test_Whatsapp(self):
        whatsapp_obj = Whatsapp()

        whatsapp_template = "whatsapp_template"
        whatsapp_obj.set_template(whatsapp_template)
        self.assertEqual(whatsapp_obj.get_template(), whatsapp_template)

        mobile = "1234567890"
        whatsapp_obj.set_mobile(mobile)
        self.assertEqual(whatsapp_obj.get_mobile(), mobile)

        whatsapp_context = "whatsapp_context"
        whatsapp_obj.set_context(whatsapp_context)
        self.assertEqual(whatsapp_obj.get_context(), whatsapp_context)

        whatsapp_obj.set_waterfall_config(Waterfall(1, 20))

        sqs_config = SqsConfig("AKIAJO4MSDD6WYU4AQRA", "AHOVq4t+C6zyUbIuIMDcVGKNeCsK50+6cD0NNZ+u",
                               "https://ap-south-1.queue.amazonaws.com/856777734734/notification-hub-dev", "ap-south-1")
        task_obj = Task(sqs_config=sqs_config)
        task_obj.set_whatsapp(whatsapp_obj)
        self.assertNotEqual(task_obj.get_whatsapp(), None)
