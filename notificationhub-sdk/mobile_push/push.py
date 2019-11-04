import protocol.notification_hub_pb2 as pb
from typing import List
from notification.common import Waterfall
import json


class Push:

    def __init__(self):
        """
        Initiates Push object
        """
        self._push = pb.Push()

    def set_template(self, template : str):
        """
        Sets push template

        Parameter:
            str

        :return:
            None
        """
        self._push.template = template

    def get_template(self) -> str:
        return self._push.template

    def del_template(self):
        del self._push.template

    def set_arn_endpoints(self, arn_endpoints: List[str]):
        """
        Sets push arnEndpoints

        Parameter:
            str

        :return:
            None
        """
        for ep in arn_endpoints:
            if isinstance(ep, str):
                self._push.arnEndpoints.append(ep)
            else:
                print("Invalid parameter; parameter should be of type List[str]")

    def get_arn_endpoints(self) -> List[str]:
        return self._push.arnEndpoints

    def del_arn_endpoints(self):
        del self._push.arnEndpoints

    def set_context(self, context: dict):
        """
        Sets push context

        Parameter:
            dict

        :return:
            None
        """
        if isinstance(context, dict):
            self._push.context = json.dumps(context)
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of type dict')

    def get_context(self) -> str:
        return self._push.context

    def del_context(self):
        del self._push.context

    def set_waterfall_config(self, waterfall: Waterfall ):
        """
        Sets push waterfall settings

        Parameter:
            str

        :return:
            None
        """
        if isinstance(waterfall, Waterfall):
            self._push.waterfallConfig.CopyFrom(waterfall.get_proto_object())
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of Waterfall')

    def get_waterfall_config(self) -> Waterfall:
        return self._push.waterfallConfig

    def del_waterfall_config(self):
        return self._push.waterfallConfig

    def set_expiry(self, expiry: float):
        """
        Sets expiry of the push

        Parameter:
            EPOCH time(float)

        :return:
            None
        """
        if isinstance(expiry, float):
            self._push.expiry = expiry
        else:
            raise ValueError('Invalid parameter passed. Parameter must be of float')

    def get_expiry(self) -> float:
        return self._push.expiry

    def del_expiry(self):
        del self._push.expiry

    def __str__(self):
        return f'template: {self._push.template}, arnEndpoints: {self._push.arnEndpoints}, context: {self._push.context}, waterfallConfig: {self._push.waterfallConfig}, expiry: {self._push.expiry}'

    def __repr__(self):
        return f'{self._push.template}, {self._push.arnEndpoints}, {self._push.context}, {self._push.waterfallConfig}, {self._push.expiry}'

    def get_proto_object(self):
        """
        :return:
            SMS protobuf object
        """
        return self._push

    def mandatory_fields_check(self) -> bool:
        """
        Checks whether all mandatory fields are set or not
        Useful before the task is pushed to SQS

        Parameter:
            None

        :return:
            bool
        """
        return self.get_arn_endpoints() and self.get_context() and self.get_template()
