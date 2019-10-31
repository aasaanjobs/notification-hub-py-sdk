import unittest
from notification.task import Task
from notification.email import Email, EmailRecipient, EmailAttachment
from notification.sms import Sms
from notification.whatsapp import Whatsapp
from notification.push import Push
from notification.common import Waterfall, MessageType, WaterfallMode
from notification.sqs_config import SqsConfig
from datetime import datetime
import uuid 


class TestNotificationTask(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        sqs_config = SqsConfig("AKIAJO4MSDD6WYU4AQRA", "AHOVq4t+C6zyUbIuIMDcVGKNeCsK50+6cD0NNZ+u", "https://ap-south-1.queue.amazonaws.com/856777734734/notification-hub-dev", "ap-south-1")
        self.task_obj = Task(sqs_config=sqs_config)

    @classmethod
    def tearDownClass(self):
        self.task_obj = None

    # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass
        
    def test_id(self):
        random_uuid = uuid.uuid1()
        self.task_obj.set_id(random_uuid)
        self.assertEqual(self.task_obj.get_id(), str(random_uuid))

    def test_name(self):
        self.task_obj.set_name("task1")
        self.assertEqual(self.task_obj.get_name(), "task1")

    def test_message_type(self):
        self.task_obj.set_message_type(MessageType.TRANSACTIONAL)
        self.assertEqual(self.task_obj.get_message_type(), MessageType.TRANSACTIONAL)

    def test_sent_by_id(self):
        random_uuid = uuid.uuid4()
        self.task_obj.set_sent_by_id(random_uuid)
        self.assertEqual(self.task_obj.get_sent_by_id(), str(random_uuid))

    def test_client(self):
        self.task_obj.set_client("xyz")
        self.assertEqual(self.task_obj.get_client(), "xyz")

    def test_triggered_on(self):
        curr_time = datetime.utcnow()
        epoch_time = datetime.timestamp(curr_time)
        self.task_obj.set_triggered_on(epoch_time)
        self.assertEqual(datetime.fromtimestamp(self.task_obj.get_triggered_on()).strftime('%Y-%m-%d %H:%M:%S.%f'), str(curr_time))

    def test_expiry(self):
        curr_time = datetime.utcnow()
        epoch_time = datetime.timestamp(curr_time)
        self.task_obj.set_expiry(epoch_time)
        self.assertEqual(datetime.fromtimestamp(self.task_obj.get_expiry()).strftime('%Y-%m-%d %H:%M:%S.%f'), str(curr_time))

   
    def test_complete_task_creation(self):
        
        # create sqs config object
        sqs_config = SqsConfig("AKIAJO4MSDD6WYU4AQRA", "AHOVq4t+C6zyUbIuIMDcVGKNeCsK50+6cD0NNZ+u", "https://ap-south-1.queue.amazonaws.com/856777734734/notification-hub-dev", "ap-south-1")

        # create task
        self.task_obj = None
        self.task_obj = Task(sqs_config=sqs_config)
        self.task_obj.set_id(uuid.uuid1())
        self.task_obj.set_name("task1")
        self.task_obj.set_message_type(MessageType.TRANSACTIONAL)
        self.task_obj.set_sent_by_id(uuid.uuid1())
        self.task_obj.set_triggered_on(datetime.timestamp(datetime.utcnow()))
        self.task_obj.set_client("python sdk")
        self.task_obj.set_waterfall_type(WaterfallMode.OVERRIDE)

        # create sms
        sms_obj = Sms()
        sms_obj.set_template("sms_template")
        sms_obj.set_mobile("9538666061")
        sms_obj.set_context("{  \"client_name\": \"Testing 1 Company\",  \"shortened_url\": \"https://www.google.com/maps/search/?api=1&query=15.5554515,73.7564752&query_place_id=ChIJOdw52ATqvzsRx4piQHNjYDM \",  \"job_link_from_website\": \"http://beta.aasaanjobs.net/candidate-zone/job/729f5abf-f725-4723-ad43-e4bfecf10449/?username=7208192788&hash_code=31d40cb782033fe14355f8d6a25a76aada3508dd577febef0ab84c9468985377&utm_source=aj_sms&utm_campaign=sfi_cn_whatsapp \",  \"interview_date\": \"21 May 19\",  \"contact_number\": \"7669662121\",  \"interview_slot\": \"11:45 AM\",  \"interview_type\": \"Face to Face Interview\",  \"job_title\": \"Test Job for Wallets page Prepaid - CNH RR AR change\",  \"client_address\": \"krislon house, Baga, North Goa\",  \"sendTo\": [    \"9082928600\"  ],  \"contact_person_name\": \"Test Company\"}")
        sms_obj.set_waterfall_config(Waterfall(1,20))
        self.task_obj.set_sms(sms_obj)

        # create email
        email_obj = Email()
        email_obj.set_template("email_template")
        email_obj.set_context("Notification Hub email context")
        email_obj.set_sender(EmailRecipient("raghavendra.nayak@olxpeople.com", "Raghav Nayak"))
        email_obj.set_subject("Notification Hub email subject")
        email_rec = EmailRecipient("raghavendra.nayak@olxpeople.com", "Raghav Nayak")
        email_obj.set_to_recipients([email_rec])
        email_obj.set_cc_recipients([email_rec])
        email_obj.set_reply_to(email_rec)

        # self.task_obj.set_whatsapp(email_obj)

        # create push
        push_Obj = Push()
        push_Obj.set_template("push_template")
        push_Obj.set_context("Notification Hub push context")
        # self.task_obj.set_push(push_obj)

        # create whatsapp
        whatsapp_obj = Whatsapp()
        whatsapp_obj.set_template("whatsapp_template")
        whatsapp_obj.set_mobile("9538666061")
        whatsapp_obj.set_context("{  \"client_name\": \"Testisssssss Company\",  \"shortened_url\": \"https://www.google.com/maps/search/?api=1&query=15.5554515,73.7564752&query_place_id=ChIJOdw52ATqvzsRx4piQHNjYDM \",  \"job_link_from_website\": \"http://beta.aasaanjobs.net/candidate-zone/job/729f5abf-f725-4723-ad43-e4bfecf10449/?username=7208192788&hash_code=31d40cb782033fe14355f8d6a25a76aada3508dd577febef0ab84c9468985377&utm_source=aj_sms&utm_campaign=sfi_cn_whatsapp \",  \"interview_date\": \"21 May 19\",  \"contact_number\": \"9538666061\",  \"interview_slot\": \"11:45 AM\",  \"interview_type\": \"Face to Face Interview\",  \"job_title\": \"Test Job for Wallets page Prepaid - CNH RR AR change\",  \"client_address\": \"krislon house, Baga, North Goa\",  \"sendTo\": [    \"9538666061\"  ],  \"contact_person_name\": \"Test Company\"}")
        whatsapp_obj.set_waterfall_config(Waterfall(1,20))
        # self.task_obj.set_whatsapp(whatsapp_obj)

        self.assertEqual(self.task_obj.push_to_sqs(), True)
     
