import protocol.notification_hub_pb2 as pb
from notification.common import Waterfall


class Whatsapp:

    def __init__(self):
        """
        Initiates Whatsapp object
        """
        self._whatsapp = pb.Whatsapp()

    def set_template(self, template : str):
        """
        Sets whatsapp template

        Parameter:
            str

        :return:
            None
        """
        self._whatsapp.template = template

    def get_template(self) -> str:
        return self._whatsapp.template

    def del_template(self):
        del self._whatsapp.template

    def set_mobile(self, mobile: str):
        """
        Sets whatsapp mobile number

        Parameter:
            str

        :return:
            None
        """
        self._whatsapp.mobile = mobile

    def get_mobile(self) -> str:
        return self._whatsapp.mobile

    def del_mobile(self):
        del self._whatsapp.mobile

    def set_context(self, context):
        """
        Sets whatsapp context

        Parameter:
            str

        :return:
            None
        """
        self._whatsapp.context = context

    def get_context(self) -> str:
        return self._whatsapp.context

    def del_context(self):
        del self._whatsapp.context

    def set_waterfall_config(self, waterfall: Waterfall ):
        """
        Sets sms waterfall settings

        Parameter:
            str

        :return:
            None
        """
        if isinstance(waterfall, Waterfall):
            self._whatsapp.waterfallConfig.CopyFrom(waterfall.get_object())
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of Waterfall')

    def get_waterfall_config(self) -> Waterfall:
        return self._whatsapp.waterfallConfig

    def del_waterfall_config(self):
        return self._whatsapp.waterfallConfig

    def set_expiry(self, expiry: float):
        """
        Sets expiry of the whatsapp

        Parameter:
            EPOCH time(float)

        :return:
            None
        """
        if isinstance(expiry, float):
            self._whatsapp.expiry = expiry
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of float')

    def get_expiry(self) -> float:
        return self._whatsapp.expiry

    def del_expiry(self):
        del self._whatsapp.expiry

    def __str__(self):
        return f'template: {self._whatsapp.template}, mobile: {self._whatsapp.mobile}, context: {self._whatsapp.context}, waterfallConfig: {self._whatsapp.waterfallConfig}, expiry: {self._whatsapp.expiry}'

    def __repr__(self):
        return f'{self._whatsapp.template}, {self._whatsapp.mobile}, {self._whatsapp.context}, {self._whatsapp.waterfallConfig}, {self._whatsapp.expiry}'

    def get_object(self):
        return self._whatsapp

    def mandatory_fields_check(self) -> bool:
        """
        Checks whether all mandatory fields are set or not
        Useful before the task is pushed to SQS

        Parameter:
            None

        :return:
            bool
        """
        return self.get_mobile() and self.get_context() and self.get_template()