from datetime import datetime

from ..proto import notification_hub_pb2 as pb

from ..common import Platform
from ..email_task import Email
from ..sms import Sms
from ..whatsapp import Whatsapp
from ..mobile_push import Push
from ..common import WaterfallMode, MessageType
from ..sqs import SQSProducer
import uuid


class Task:
    """
    A wrapper class for NotificationTask protobuf structure
    """

    def __init__(self, name: str, send_by_id: str, client: str, platform: Platform,
                 message_type: MessageType = MessageType.MARKETING, email: Email = None, sms: Sms = None,
                 whatsapp: Whatsapp = None, push: Push = None, waterfall_type: WaterfallMode = WaterfallMode.AUTO):
        """
        Initiates the task object
        :key name: Notification name (should be unique)
        :key send_by_id: ID of the user who triggered the notification
        :key platform: Which company vertical are we sending to
        :key message_type: Nature of medium of the notification
        """
        self._task = pb.NotificationTask()

        # Check whether at least one channel is specified
        if not email and not sms and not whatsapp and not push:
            raise AssertionError('Atleast one channel should be passed')
        self.__set_id()
        self.__set_triggered_on()

        self._task.name = name
        self._task.sentByID = send_by_id
        self._task.client = client
        self._task.platform = platform
        self._task.messageType = message_type
        self._task.waterfallType = waterfall_type

        # Assign the notification channels
        self.__set_sms(sms)
        self.__set_email(email)
        self.__set_whatsapp(whatsapp)
        self.__set_push(push)

    def __set_id(self):
        """
        Generates a UUID v4 and assigns the value as ID
        """
        self._task.ID = str(uuid.uuid4())

    def __set_triggered_on(self):
        """
        Sets the current timestamp as triggered on
        """
        utc_now = datetime.utcnow()
        self._task.triggeredOn = int(datetime.timestamp(utc_now))

    def __set_sms(self, value: Sms):
        if not value:
            return
        self._task.sms.CopyFrom(value.proto)

    def __set_email(self, value: Email):
        if not value:
            return
        self._task.email.CopyFrom(value.proto)

    def __set_whatsapp(self, value: Whatsapp):
        if not value:
            return
        self._task.whatsapp.CopyFrom(value.proto)

    def __set_push(self, value: Push):
        if not value:
            return
        self._task.push.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.NotificationTask:
        return self._task

    def send(self, **kwargs):
        producer = SQSProducer(**kwargs)
        producer.send_message(self._task)
