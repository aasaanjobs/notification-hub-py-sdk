import unittest
from .whatsapp import Whatsapp
from .common import Waterfall
from .task import Task
from .sqs_config import SqsConfig
from .env_file_settings import *
import json


class TestWhatsapp(unittest.TestCase):

    def test_Whatsapp(self):
        whatsapp_obj = Whatsapp()

        whatsapp_template = "whatsapp_template"
        whatsapp_obj.set_template(whatsapp_template)
        self.assertEqual(whatsapp_obj.get_template(), whatsapp_template)

        mobile = "1234567890"
        whatsapp_obj.set_mobile(mobile)
        self.assertEqual(whatsapp_obj.get_mobile(), mobile)

        whatsapp_context = {  "client_name": "Testisssssss Company",  "shortened_url": "https://www.google.com/maps/search/?api=1&query=15.5554515,73.7564752&query_place_id=ChIJOdw52ATqvzsRx4piQHNjYDM ",  "job_link_from_website": "http://beta.aasaanjobs.net/candidate-zone/job/729f5abf-f725-4723-ad43-e4bfecf10449/?username=7208192788&hash_code=31d40cb782033fe14355f8d6a25a76aada3508dd577febef0ab84c9468985377&utm_source=aj_sms&utm_campaign=sfi_cn_whatsapp ",  "interview_date": "21 May 19",  "contact_number": "7669662121",  "interview_slot": "11:45 AM",  "interview_type": "Face to Face Interview",  "job_title": "Test Job for Wallets page Prepaid - CNH RR AR change",  "client_address": "krislon house, Baga, North Goa",  "sendTo": [    "9082928600"  ],  "contact_person_name": "Test Company"}
        whatsapp_obj.set_context(whatsapp_context)
        self.assertEqual(whatsapp_obj.get_context(), json.dumps(whatsapp_context))

        whatsapp_obj.set_waterfall_config(Waterfall(1, 20))

        # create task obj
        self.assertTrue(load_sqs_settings())
        sqs_config = SqsConfig(SQS_ACCESS_KEY_ID,
                               SQS_SECRET_ACCESS_KEY,
                               SQS_QUEUE_URL,
                               SQS_REGION)
        task_obj = Task(sqs_config=sqs_config)
        task_obj.set_whatsapp(whatsapp_obj)
        self.assertNotEqual(task_obj.get_whatsapp(), None)
