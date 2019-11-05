import unittest

from common import Platform
from .email import Email, EmailRecipient, EmailAttachment


class TestEmailRecipient(unittest.TestCase):

    def test_EmailRecipient(self):
        email_id = "abc@olxpeople.com"
        name = "sample_email"
        email_reci_obj = EmailRecipient(email_id, name)

        self.assertEqual(email_reci_obj.proto.email, email_id)

        self.assertEqual(email_reci_obj.proto.name, name)


class TestEmailAttachment(unittest.TestCase):

    def test_EmailAttachment(self):
        file = "abc.txt"
        url = "google.com"
        email_attach_obj = EmailAttachment(file, url)
        self.assertEqual(email_attach_obj.proto.filename, file)
        self.assertEqual(email_attach_obj.proto.url, url)


class TestEmail(unittest.TestCase):

    def test_Email(self):
        send_to = EmailRecipient('john.doe@example.com', 'John Doe')
        subject = 'Testing Email'
        template = 'https://www.aasaanjobs.com/static.html'
        email_obj = Email([send_to], template, subject, Platform.Aasaanjobs)

        # Test Template
        self.assertEqual(email_obj.proto.template, template)
        # Test Subject
        self.assertEqual(email_obj.proto.subject, subject)
        # Test recipients
        self.assertEqual(email_obj.proto.toRecipients[0].email, send_to.proto.email)
