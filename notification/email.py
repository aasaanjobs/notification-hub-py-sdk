import protocol.notification_hub_pb2 as pb
from typing import List
from notification.common import Waterfall


class EmailRecipient:

    def __init__(self, email: str = "", name: str = ""):
        """
        Initiates EmailRecipient object
        """
        self._email_recipient = pb.Email.EmailRecipient()
        self._email_recipient.email = email
        self._email_recipient.name = name

    def set_email(self, email: str):
        """
        Sets email id of EmailRecipient

        Parameter:
            str

        :return:
            None
        """
        self._email_recipient.email = email

    def get_email(self) -> str:
        return self._email_recipient.email

    def del_email(self):
        del self._email_recipient.email

    def set_name(self, name: str):
        """
        Sets name of EmailRecipient

        Parameter:
            str

        :return:
            None
        """
        self._email_recipient.name = name

    def get_name(self) -> str:
        return self._email_recipient.name

    def del_name(self):
        del self._email_recipient.name

    def __str__(self):
        return f'email: {self._email_recipient.email}, name: {self._email_recipient.name}'

    def __repr__(self):
        return f'{self._email_recipient.email}, {self._email_recipient.name}'
    
    def get_object(self):
        """
        :returns
            EmailRecipient object
        """
        return self._email_recipient

    def mandatory_fields_check(self) -> bool:
        """
        Checks whether all mandatory fields are set or not
        Useful before the task is pushed to SQS

        Parameter:
            None

        :return:
            bool
        """
        return self.get_email()


class EmailAttachment:

    def __init__(self, file_name: str = "" , url: str = ""):
        """
        Initiates EmailAttachment object
        """
        self._email_attachment = pb.Email.EmailAttachment()
        self._email_attachment.filename = file_name
        self._email_attachment.url = url

    def set_file_name(self, file_name: str):
        """
        Sets name of EmailAttachment

        Parameter:
            str

        :return:
            None
        """
        self._email_attachment.filename = file_name

    def get_file_name(self) -> str:
        return self._email_attachment.filename

    def del_file_name(self):
        del self._email_attachment.file_name

    def set_url(self, url):
        """
        Sets url of EmailAttachment

        Parameter:
            str

        :return:
            None
        """
        self._email_attachment.url = url

    def get_url(self) -> str:
        return self._email_attachment.url

    def del_url(self):
        del self._email_attachment.url

    def __str__(self):
        return f'attachment: {self._email_attachment.filename}, url: {self._email_attachment.url}'

    def __str__(self):
        return f'{self._email_attachment.filename}, {self._email_attachment.url}'

    def get_object(self):
        """
        :returns
            EmailAttachment object
        """
        return self._email_attachment

    def mandatory_fields_check(self) -> bool:
        """
        Checks whether all mandatory fields are set or not
        Useful before the task is pushed to SQS

        Parameter:
            None

        :return:
            bool
        """
        return self.get_file_name() and self.get_url()


class Email:

    def __init__(self):
        """
        Initiates Email object
        """
        self._email = pb.Email()

    def set_template(self, template: str):
        """
        Sets email template

        Parameter:
            str

        :return:
            None
        """
        self._email.template = template

    def get_template(self) -> str:
        return self._email.template

    def del_template(self):
        del self._email.template

    def set_to_recipients(self, email_recipients: List[EmailRecipient]):
        """
        Sets email toRecipients

        Parameter:
            list of EmailRecipient

        :return:
            None
        """
        for email_reci in email_recipients:
            if isinstance(email_reci, EmailRecipient):
                if email_reci.mandatory_fields_check():
                    self._email.toRecipients.append(email_reci.get_object())
                else:
                    raise ValueError('Mandatory fields of EmailRecipient are not set')
            else:
                print("In set_to_recipients(), Invalid parameter; parameter should be of type EmailRecipient")

    def get_to_recipients(self) -> List[EmailRecipient]:
        return self._email.toRecipients

    def del_to_recipients(self):
        del self._email.toRecipients

    def set_context(self, context: str):
        """
        Sets email context

        Parameter:
            str

        :return:
            None
        """
        self._email.context = context

    def get_context(self) -> str:
        return self._email.context

    def del_context(self):
        del self._email.context

    def set_subject(self, subject: str):
        """
        Sets email subject

        Parameter:
            str

        :return:
            None
        """
        self._email.subject = subject

    def get_subject(self) -> str:
        return self._email.subject

    def del_subject(self):
        del self._email.subject

    def set_sender(self, sender: EmailRecipient):
        """
        Sets email sender

        Parameter:
            EmailRecipient

        :return:
            None
        """
        if isinstance(sender, EmailRecipient):
            if sender.mandatory_fields_check():
                self._email.sender.CopyFrom(sender.get_object())
            else:
                raise ValueError('Mandatory fields of EmailRecipient are not set')
        else:
            print("In set_sender(), Invalid parameter; parameter should be of type EmailRecipient")

    def get_sender(self) -> EmailRecipient:
        return self._email.sender

    def del_sender(self):
        del self._email.sender

    def set_reply_to(self, reply_to: EmailRecipient):
        """
        Sets email replyTo

        Parameter:
            EmailRecipient

        :return:
            None
        """
        if isinstance(reply_to, EmailRecipient):
            if reply_to.mandatory_fields_check():
                self._email.replyTo.CopyFrom(reply_to.get_object())
            else:
                raise ValueError('Mandatory fields of EmailRecipient are not set')
        else:
            print("In set_reply_to, Invalid parameter; parameter should be of type EmailRecipient")

    def get_reply_to(self) -> EmailRecipient:
        return self._email.replyTo

    def del_reply_to(self):
        del self._email.replyTo

    def set_cc_recipients(self, email_recipients: List[EmailRecipient]):
        """
        Sets email ccRecipients

        Parameter:
            list of EmailRecipient

        :return:
            None
        """
        for email_reci in email_recipients:
            if isinstance(email_reci, EmailRecipient):
                if email_reci.mandatory_fields_check():
                    self._email.ccRecipients.append(email_reci.get_object())
                else:
                    raise ValueError('Mandatory fields of EmailRecipient are not set')
            else:
                print("In set_cc_recipients, Invalid parameter; parameter should be of type EmailRecipient")

    def get_cc_recipients(self) -> List[EmailRecipient]:
        return self._email.ccRecipients

    def del_cc_recipients(self):
        del self._email.ccRecipients

    def set_attachments(self, attachments: List[EmailAttachment]):
        """
        Sets email attachments

        Parameter:
            list of EmailAttachment

        :return:
            None
        """
        for email_attach in attachments:
            if isinstance(email_attach, EmailAttachment):
                if email_attach.mandatory_fields_check():
                    self._email.attachments.append(email_attach.get_object())
                else:
                    raise ValueError('Mandatory fields of EmailAttachment are not set')
            else:
                print("Invalid parameter; parameter should be of type EmailAttachment")

    def get_attachments(self) -> List[EmailAttachment]:
        return self._email.attachments

    def del_attachments(self):
        del self._email.attachments

    def set_waterfall_config(self, waterfall: Waterfall):
        """
        Sets email waterfall settings

        Parameter:
            str

        :return:
            None
        """
        if isinstance(waterfall, Waterfall):
            self._email.waterfallConfig.CopyFrom(waterfall.get_object())
        else:
            print("Invalid parameter; parameter should be of type Waterfall")

    def get_waterfall_config(self) -> Waterfall:
        return self._email.waterfallConfig

    def del_waterfall_config(self):
        return self._email.waterfallConfig

    def set_expiry(self, expiry: float):
        """
        Sets expiry of the email

        Parameter:
            EPOCH time(float)

        :return:
            None
        """
        if isinstance(expiry, float):
            self._email.expiry = expiry
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of float')

    def get_expiry(self) -> float:
        return self._email.expiry

    def del_expiry(self):
        del self._email.expiry

    def __str__(self):
        return f'template: {self._email.template}, toRecipients: {self._email.toRecipients}, context: {self._email.context}, subject: {self._email.subject}, sender: {self._email.sender}, replyTo: {self._email.replyTo}, ccRecipients: {self._email.ccRecipients}, attachments: {self._email.attachments}, waterfallConfig: {self._email.waterfallConfig}, expiry: {self._email.expiry}'

    def __repr__(self):
        return f'{self._email.template}, {self._email.toRecipients}, {self._email.context}, {self._email.subject}, {self._email.sender}, {self._email.replyTo}, {self._email.ccRecipients}, {self._email.attachments}, {self._email.waterfallConfig}, {self._email.expiry}'

    def get_object(self):
        """
        :return:
            Email protobuf object
        """
        return self._email

    def mandatory_fields_check(self) -> bool:
        """
        Checks whether all mandatory fields are set or not
        Useful before the task is pushed to SQS

        Parameter:
            None

        :return:
            bool
        """
        return  self.set_template and self.get_subject() and self.get_context and self.get_sender() and self.get_to_recipients() and self.get_reply_to()