import unittest

from base import InvalidEmail, InvalidAttachmentUrl
from common import Platform
from .email import Email, EmailRecipient, EmailAttachment


class TestEmailRecipient(unittest.TestCase):
    def setUp(self):
        self.correct_email = 'john.doe@olxpeople.com'
        self.recipient_name = 'John Doe'
        self.incorrect_email = 'john.doe.olxpeople.com'

    def test_correct_email(self):
        obj = EmailRecipient(self.correct_email, self.recipient_name)
        self.assertEqual(obj.proto.email, self.correct_email)

    def test_incorrect_email(self):
        with self.assertRaises(InvalidEmail):
            EmailRecipient(self.incorrect_email, self.recipient_name)

    def test_recipient_name(self):
        obj = EmailRecipient(self.correct_email, self.recipient_name)
        self.assertEqual(obj.proto.name, self.recipient_name)


class TestEmailAttachment(unittest.TestCase):
    def setUp(self) -> None:
        self.file = "abc.txt"
        self.correct_url = "https://static.aasaanjobs.com/static/abc.txt"
        self.incorrect_url = "sample_file.txt"

    def test_correct_file_url(self):
        obj = EmailAttachment(self.file, self.correct_url)
        self.assertEqual(obj.proto.url, self.correct_url)

    def test_incorrect_file_url(self):
        with self.assertRaises(InvalidAttachmentUrl):
            EmailAttachment(self.file, self.incorrect_url)

    def test_attachment_name(self):
        obj = EmailAttachment(self.file, self.correct_url)
        self.assertEqual(obj.proto.filename, self.file)


class TestEmail(unittest.TestCase):
    def setUp(self) -> None:
        self.recipient = EmailRecipient('john.doe@olxpeople.com', 'John Doe')
        self.attachment = EmailAttachment('abc.txt', "https://static.aasaanjobs.com/static/abc.txt")
        self.subject = 'Test Email'
        self.correct_template = 'https://static.aasaanjobs.com/email_template.html'
        self.incorrect_template = 'email_template.html'

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
