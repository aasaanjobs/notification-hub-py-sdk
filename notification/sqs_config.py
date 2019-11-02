class SqsConfig:

    def __init__(self, access_key_id, secret_access_key, queue_url, region):
        """
        to get SQS config
        used by SqsProducer to initiates session and send message
        """
        self._access_key_id = access_key_id
        self._secret_access_key = secret_access_key
        self._queue_url = queue_url
        self._region = region

    def get_access_key_id(self) -> str:
        """
        :return:
            access key id of SQS
        """
        return self._access_key_id

    def get_secret_access_key(self) -> str:
        """
        :return:
            secret access key of SQS
        """
        return self._secret_access_key

    def get_queue_url(self) -> str:
        """
        :return:
            queue url of SQS
        """
        return self._queue_url

    def get_region(self) -> str:
        """
        :return:
            region of SQS
        """
        return self._region
