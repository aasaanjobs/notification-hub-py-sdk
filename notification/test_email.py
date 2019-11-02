import unittest
from .email import Email, EmailRecipient, EmailAttachment
from .task import Task
from .sqs_config import SqsConfig
from .env_file_settings import *
import json


class TestEmailRecipient(unittest.TestCase):

    def test_EmailRecipient(self):
        email_reci_obj = EmailRecipient()
        email_id = "abc@olxpeople.com"
        email_reci_obj.set_email(email_id)
        self.assertEqual(email_reci_obj.get_email(), email_id)

        name = "sample_email"
        email_reci_obj.set_name(name)
        self.assertEqual(email_reci_obj.get_name(), name)


class TestEmailAttachment(unittest.TestCase):

    def test_EmailAttachment(self):
        email_attach_obj = EmailAttachment()

        file = "abc.txt"
        email_attach_obj.set_file_name(file)
        self.assertEqual(email_attach_obj.get_file_name(), file)

        url = "goole.com"
        email_attach_obj.set_url(url)
        self.assertEqual(email_attach_obj.get_url(), url)


class TestEmail(unittest.TestCase):

    def test_Email(self):
        email_obj = Email()

        email_template = "email_template"
        email_obj.set_template(email_template)
        self.assertEqual(email_obj.get_template(), email_template)

        email_context = {  "client_name": "Testisssssss Company",  "shortened_url": "https://www.google.com/maps/search/?api=1&query=15.5554515,73.7564752&query_place_id=ChIJOdw52ATqvzsRx4piQHNjYDM ",  "job_link_from_website": "http://beta.aasaanjobs.net/candidate-zone/job/729f5abf-f725-4723-ad43-e4bfecf10449/?username=7208192788&hash_code=31d40cb782033fe14355f8d6a25a76aada3508dd577febef0ab84c9468985377&utm_source=aj_sms&utm_campaign=sfi_cn_whatsapp ",  "interview_date": "21 May 19",  "contact_number": "7669662121",  "interview_slot": "11:45 AM",  "interview_type": "Face to Face Interview",  "job_title": "Test Job for Wallets page Prepaid - CNH RR AR change",  "client_address": "krislon house, Baga, North Goa",  "sendTo": [    "9082928600"  ],  "contact_person_name": "Test Company"}
        email_obj.set_context(email_context)
        self.assertEqual(email_obj.get_context(), json.dumps(email_context))

        email_subject = "Notification Hub email subject"
        email_obj.set_subject(email_subject)
        self.assertEqual(email_obj.get_subject(), email_subject)

        email_recipient = EmailRecipient("abc@olxpeople.com", "abc xyz")
        email_obj.set_sender(email_recipient)
        # self.assertEqual(email_obj.get_sender(), email_recipient)

        email_obj.set_to_recipients([email_recipient])
        # self.assertEqual(email_obj.get_to_recipients().get_email(), email_recipient.get_email())

        email_obj.set_cc_recipients([email_recipient])
        # self.assertEqual(email_obj.get_cc_recipients().get_email(), email_recipient.get_email())

        email_obj.set_reply_to(email_recipient)
        # self.assertEqual(email_obj.get_reply_to().get_email(), email_recipient.get_email())

        # create task obj
        self.assertTrue(load_sqs_settings())
        sqs_config = SqsConfig(SQS_ACCESS_KEY_ID,
                               SQS_SECRET_ACCESS_KEY,
                               SQS_QUEUE_URL,
                               SQS_REGION)
        task_obj = Task(sqs_config=sqs_config)
        task_obj.set_email(email_obj)
        self.assertNotEqual(task_obj.get_email(), None)
        
        

