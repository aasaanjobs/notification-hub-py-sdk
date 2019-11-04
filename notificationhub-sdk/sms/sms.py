import json

from base import get_expiry, validate_template
from common import Waterfall
from proto import notification_hub_pb2 as pb


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
        self._sms.mobile = send_to

        validate_template(template)
        self._sms.template = template

        self._sms.context = json.dumps(context) if context else '{}'
        self._sms.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)
        self._sms.waterfallConfig = waterfall_config if waterfall_config else Waterfall().proto

    @property
    def proto(self) -> pb.SMS:
        return self._sms
