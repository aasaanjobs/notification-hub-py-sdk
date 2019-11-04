from protocol.notification_hub_pb2 import NotificationTask
from .email import Email
from .sms import Sms
from .whatsapp import Whatsapp
from notification.push import Push
from notification.common import WaterfallMode, MessageType
from notification.sqs_config import SqsConfig
from notification.sqs import SqsProducer
import uuid

class Task:
    """
    A wrapper class for NotificationTask protobuf structure
    """

    def __init__(self, *args, **kwargs):
        """
        Initiates the task object

        Parameter:
            SqsConfig object

        Raises:
            ValueError exception
        """
        self._task = NotificationTask()
        self._sqs_config = kwargs.get('sqs_config')
        if not isinstance(self._sqs_config, SqsConfig):
            raise ValueError('Invalid SQS config!!')


    def set_id(self, uuid_obj: uuid):
        """
        Sets passed uuid to task ID as str

        Parameter:
            uuid

        Raises:
            ValueError exception

        :return:
            None
        """
        if isinstance(uuid_obj, uuid.UUID):
            self._task.ID = str(uuid_obj)
        else:
             raise ValueError('Invalid parameter passed. Parameter must be of type uuid')


    def get_id(self) -> str:
        return self._task.ID


    def del_id(self):
        del self._task.ID

    def set_name(self, name: str):
        """
        Sets name of the task

        Parameter:
            str

        :return:
            None
        """
        if isinstance(name, str):
            self._task.name = name
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of str')


    def get_name(self) -> str:
        return self._task.name

    def del_name(self):
        del self._task.name


    def set_message_type(self, message_type: MessageType = MessageType.MARKETING):
        """
        Sets messageType of the task
        message_type : possible options 0(MARKETING) / 1(TRANSACTIONAL)

        Parameter:
            MessageType or int

        Raises:
            ValueError exception

        :return:
            None
        """
        if isinstance(message_type, MessageType):
            self._task.messageType = message_type
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type MessageType')

    def get_message_type(self) -> int:
        return self._task.messageType

    def del_message_type(self):
        del self._task.messageType

    def set_email(self, email: Email = None):
        """
        Sets task email

        Parameter:
            Email

        :return:
            None
        """
        if isinstance(email, Email):
            if email.mandatory_fields_check():
                self._task.email.CopyFrom(email.get_proto_object())
            else:
                raise ValueError('Mandatory fields of Email are not set')
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type Email')

    def get_email(self) -> Email:
        return self._task.email

    def del_email(self):
        del self._task.email

    def set_sms(self, sms: Sms = None):
        """
        Sets task sms

        Parameter:
            Sms

        :return:
            None
        """
        if isinstance(sms, Sms):
            if sms.mandatory_fields_check():
                self._task.sms.CopyFrom(sms.get_proto_object())
            else:
                raise ValueError('Mandatory fields of Sms are not set')
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type Sms')

    def get_sms(self) -> Sms:
        return self._task.sms

    def del_sms(self):
        del self._task.sms

    def set_whatsapp(self, whatsapp: Whatsapp = None):
        """
        Sets task whatsapp

        Parameter:
            Whatsapp

        :return:
            None
        """
        if isinstance(whatsapp, Whatsapp):
            if whatsapp.mandatory_fields_check():
                self._task.whatsapp.CopyFrom(whatsapp.get_proto_object())
            else:
                raise ValueError('Mandatory fields of Whatsapp are not set')
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type Whatsapp')

    def get_whatsapp(self) -> Whatsapp:
        return self._task.whatsapp

    def del_whatsapp(self):
        del self._task.whatsapp

    def set_push(self, push : Push = None):
        """
        Sets task push

        Parameter:
            Push

        :return:
            None
        """
        if isinstance(push, Push):
            if push.mandatory_fields_check():
                self._task.push.CopyFrom(push.get_proto_object())
            else:
                raise ValueError('Mandatory fields of Push are not set')
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type Push')

    def get_push(self) -> Push:
        return self._task.push

    def del_push(self):
        del self._task.push

    def set_sent_by_id(self, sent_by_id):
        """
        Sets passed uuid to task sentByID as str

        Parameter:
            uuid

        Raises:
            ValueError exception

        :return:
            None
        """
        if isinstance(sent_by_id, uuid.UUID):
            self._task.sentByID = str(sent_by_id)
        else:
             raise ValueError('Invalid parameter passed. Parameter must be of type uuid')

    def get_sent_by_id(self) -> str:
        return self._task.sentByID

    def del_sent_by_id(self):
        del self._task.sentByID

    def set_client(self, client: str):
        """
        Sets client

        Parameter:
            str

        :return:
            None
        """
        if isinstance(client, str):
            self._task.client = client
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of str')

    def get_client(self) -> str:
        return self._task.client

    def del_client(self):
        del self._task.client

    def set_waterfall_type(self, waterfall_type: WaterfallMode = WaterfallMode.AUTO):
        """
        Sets waterfallType of task
        WaterfallMode : possible options 0(AUTO) / 1(OVERRIDE)

        Parameter:
            WaterfallMode

        :return:
            None
        """
        if isinstance(waterfall_type, WaterfallMode):
            self._task.waterfallType = waterfall_type
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of WaterfallMode')


    def get_waterfall_type(self) -> WaterfallMode:
        return self._task.waterfallType

    def del_waterfall_type(self):
        del self._task.waterfallType

    def set_triggered_on(self, triggered_on: float):
        """
        Sets triggeredOn

        Parameter:
            EPOCH time(float)

        :return:
            None
        """
        if isinstance(triggered_on, float):
            self._task.triggeredOn = float(triggered_on)
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of float')

    def get_triggered_on(self) -> float:
        return self._task.triggeredOn

    def del_triggered_on(self):
        del self._task.triggeredOn

    def set_expiry(self, expiry: float):
        """
        Sets expiry of the task

        Parameter:
            EPOCH time(float)

        :return:
            None
        """
        if isinstance(expiry, float):
            self._task.expiry = expiry
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of float')

    def get_expiry(self) -> float:
        return self._task.expiry

    def del_expiry(self):
        del self._task.expiry

    def __str__(self):
         return f'id: {self._task.ID}, name: {self._task.name}, messageType: {self._task.messageType}, sent_by_id: {self._task.sentByID}, client: {self._task.client}, waterfall_type: {self._task.waterfallType}, expiry: {self._task.expiry}, email: {self._task.email}, sms: {self._task.sms}, whatsapp: {self._task.whatsapp}, push: {self._task.push}'

    def __repr__(self):
         return f'{self._task.ID}, {self._task.name}, {self._task.messageType}, {self._task.sentByID}, {self._task.client}, {self._task.waterfallType}, {self._task.expiry}, {self._task.email}, {self._task.sms}, {self._task.whatsapp}, {self._task.push}'

    def get_proto_object(self) -> NotificationTask :
        """
        :return:
            NotificationTask protobuf object
        """
        return self._task

    def get_serialized_string(self):
        """
        currently we are not serializing. So, it returns the Notification protobuf object.
        :return:
            seriliazed NotificationTask protobuf object
        """
        return self._task

    def mandatory_fields_check(self) -> bool:
        """
        Checks whether all mandatory fields are set or not
        Useful before the task is pushed to SQS
        At least one of sms/email/whatsapp/push should be set

        Parameter:
            None

        :return:
            bool
        """
        return self.get_id() and self.get_name() and self.get_waterfall_type() and  self.get_triggered_on() and \
            (self.get_sms() and self.get_sms()or self.get_email() or self.get_whatsapp() or self.get_push())

    def push_to_sqs(self) -> bool:
        """
        Push the task object to SQS by calling SqsProducer
        Pre-condition checks:
            Mandatory fields should be set
            SqsConfig should be set

        Parameter:
            None

        :return:
            bool (success or failure of send message)
        """
        return_value = False

        # check all the mandatory fields are filled
        if self.mandatory_fields_check():
            # currently, we are sending string instead of serialized string.
            serialized_string = self.get_serialized_string()

            producer = SqsProducer(sqs_config= self._sqs_config)
            if producer.send_message(serialized_string):
                return_value =  True
        else:
            raise ValueError("Error!! mandatory fields of tasks are not set!! Set all the mandatory fields before you send message to SQS")
        return return_value


