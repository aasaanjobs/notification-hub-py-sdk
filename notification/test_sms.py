import unittest
from .sms import Sms
from .common import Waterfall
from .task import Task
from .sqs_config import SqsConfig
from .env_file_settings import *
import json


class TestSms(unittest.TestCase):

    def test_Sms(self):
        sms_obj = Sms()

        sms_template = "sms_template"
        sms_obj.set_template(sms_template)
        self.assertEqual(sms_obj.get_template(), sms_template)

        mobile = "1234567890"
        sms_obj.set_mobile(mobile)
        self.assertEqual(sms_obj.get_mobile(), mobile)

        sms_context = {  "client_name": "Testisssssss Company",  "shortened_url": "https://www.google.com/maps/search/?api=1&query=15.5554515,73.7564752&query_place_id=ChIJOdw52ATqvzsRx4piQHNjYDM ",  "job_link_from_website": "http://beta.aasaanjobs.net/candidate-zone/job/729f5abf-f725-4723-ad43-e4bfecf10449/?username=7208192788&hash_code=31d40cb782033fe14355f8d6a25a76aada3508dd577febef0ab84c9468985377&utm_source=aj_sms&utm_campaign=sfi_cn_whatsapp ",  "interview_date": "21 May 19",  "contact_number": "7669662121",  "interview_slot": "11:45 AM",  "interview_type": "Face to Face Interview",  "job_title": "Test Job for Wallets page Prepaid - CNH RR AR change",  "client_address": "krislon house, Baga, North Goa",  "sendTo": [    "9082928600"  ],  "contact_person_name": "Test Company"}
        sms_obj.set_context(sms_context)
        self.assertEqual(sms_obj.get_context(), json.dumps(sms_context))

        sms_obj.set_waterfall_config(Waterfall(1, 20))

        # create task obj
        sqs_config = load_sqs_settings()
        self.assertIsNotNone(sqs_config)
        sqs_config = SqsConfig(sqs_config["SQS_ACCESS_KEY_ID"],
                               sqs_config["SQS_SECRET_ACCESS_KEY"],
                               sqs_config["SQS_QUEUE_URL"],
                               sqs_config["SQS_REGION"])
        task_obj = Task(sqs_config=sqs_config)
        task_obj.set_sms(sms_obj)
        self.assertNotEqual(task_obj.get_sms(), None)
