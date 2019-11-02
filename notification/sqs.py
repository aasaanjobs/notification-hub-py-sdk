import boto3
from .sqs_config import SqsConfig


class SqsProducer:
    """
    Used for pushing the messages to SQS
    """

    def __init__(self, *args, **kwargs):
        """
        Initiates Sms object
        """
        self._notification_sqs = None
        self._queue = None
        self._sqs_config = kwargs.get('sqs_config')
        if self._sqs_config is None or not isinstance(self._sqs_config, SqsConfig):
            raise ValueError('Invalid SQS config!!')
        self.init_sqs_session()
    
    def init_sqs_session(self):
        """
        Initiates SQS session and queue

        Parameter:
            None

        :return:
            None
        """
        self._notification_sqs = boto3.resource(
            service_name = "sqs",
            aws_access_key_id = self._sqs_config.get_access_key_id(),
            aws_secret_access_key = self._sqs_config.get_secret_access_key(),
            region_name = self._sqs_config.get_region()
        )

        for queue in self._notification_sqs.queues.all():
            if queue.url == self._sqs_config.get_queue_url():
                self._queue = queue
        if self._queue is None:
            raise ValueError('Invalid SQS URL given in the SQS config object!!')

    def send_message(self, message_body: str) -> bool:
        """
        sends a message to SQS

        Parameter:
            message to be sent to SQS (str)

        :return:
            None
        """
        send_message_status = False

        print("message body : ", message_body)

        try:
            response = self._queue.send_message(
                QueueUrl=self._queue.url,
                MessageBody=str(message_body)
            )

            HTTPStatusCode = response.get('ResponseMetadata').get('HTTPStatusCode')
            if HTTPStatusCode in [200, 201, 202, 203, 204]:
                send_message_status = True
            else:
                print("Error while sending the message to SQS notification queue", response)
        except RuntimeError:
            print("RuntimeError while sending message to SQS")

        return send_message_status

        



