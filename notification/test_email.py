import unittest
from notification.email import Email, EmailRecipient, EmailAttachment
from notification.task import Task
from notification.sqs_config import SqsConfig


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

        email_context = "Notification Hub email context"
        email_obj.set_context(email_context)
        self.assertEqual(email_obj.get_context(), email_context)

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

        sqs_config = SqsConfig("AKIAJO4MSDD6WYU4AQRA", "AHOVq4t+C6zyUbIuIMDcVGKNeCsK50+6cD0NNZ+u",
                               "https://ap-south-1.queue.amazonaws.com/856777734734/notification-hub-dev", "ap-south-1")
        task_obj = Task(sqs_config=sqs_config)
        task_obj.set_email(email_obj)
        self.assertNotEqual(task_obj.get_email(), None)
        
        

