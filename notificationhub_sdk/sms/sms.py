import json

from ..base import get_expiry, validate_template, validate_mobile
from ..common import Waterfall
from ..proto import notification_hub_pb2 as pb


class Sms:
    _default_expiry_offset = 7  # 7 Days

    def __init__(
            self,
            send_to: str,
            template: str,
            context: dict = None,
            waterfall_config: Waterfall = None,
            expiry: int = None
    ):
        """
        Initiates Sms object
        """
        self._sms = pb.SMS()

        validate_mobile(send_to)
        self._sms.mobile = send_to

        validate_template(template)
        self._sms.template = template

        self._sms.context = json.dumps(context) if context else '{}'
        self._sms.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)

        self.__set_waterfall(waterfall_config)

    def __set_waterfall(self, value: Waterfall = None):
        if not value:
            value = Waterfall()
        self._sms.waterfallConfig.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.SMS:
        return self._sms
