import protocol.notification_hub_pb2 as pb
from notification.common import Waterfall
import json


class Sms:

    def __init__(self):
        """
        Initiates Sms object
        """
        self._sms = pb.SMS()

    def set_template(self, template : str):
        """
        Sets sms template

        Parameter:
            str

        :return:
            None
        """
        if isinstance(template, str):
            self._sms.template = template
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type str')

    def get_template(self) -> str:
        return self._sms.template

    def del_template(self):
        del self._sms.template

    def set_mobile(self, mobile: str):
        """
        Sets sms mobile number

        Parameter:
            str

        :return:
            None
        """
        if isinstance(mobile, str):
            self._sms.mobile = mobile
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type str')

    def get_mobile(self) -> str:
        return self._sms.mobile

    def del_mobile(self):
        del self._sms.mobile

    def set_context(self, context: dict):
        """
        Sets sms context

        Parameter:
            dict

        :return:
            None
        """
        if isinstance(context, dict):
            self._sms.context = json.dumps(context)
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type dict')

    def get_context(self) -> str:
        return self._sms.context

    def del_context(self):
        del self._sms.context


    def set_waterfall_config(self, waterfall: Waterfall ):
        """
        Sets sms waterfall settings

        Parameter:
            str

        :return:
            None
        """
        if isinstance(waterfall, Waterfall):
            self._sms.waterfallConfig.CopyFrom(waterfall.get_proto_object())
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of Waterfall')

    def get_waterfall_config(self) -> Waterfall:
        return self._sms.waterfallConfig

    def del_waterfall_config(self):
        return self._sms.waterfallConfig

    def set_expiry(self, expiry: float):
        """
        Sets expiry of the sms

        Parameter:
            EPOCH time(float)

        :return:
            None
        """
        if isinstance(expiry, float):
            self._sms.expiry = expiry
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of float')

    def get_expiry(self) -> float:
        return self._sms.expiry

    def del_expiry(self):
        del self._sms.expiry

    def __str__(self):
        return f'template: {self._sms.template}, mobile: {self._sms.mobile}, context: {self._sms.context}, waterfallConfig: {self._sms.waterfallConfig}, expiry: {self._sms.expiry}'

    def __repr__(self):
        return f'{self._sms.template}, {self._sms.mobile}, {self._sms.context}, {self._sms.waterfallConfig}, {self._sms.expiry}'

    def get_proto_object(self):
        """
        :return:
            SMS protobuf object
        """
        return self._sms

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
