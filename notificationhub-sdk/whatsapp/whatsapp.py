import json

from base import validate_template, get_expiry
from common import Waterfall
from proto import notification_hub_pb2 as pb


class Whatsapp:
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
        Initiates Whatsapp object
        """
        self._whatsapp = pb.Whatsapp()
        self._whatsapp.mobile = send_to

        validate_template(template)
        self._whatsapp.template = template

        self._whatsapp.context = json.dumps(context) if context else '{}'

        self._whatsapp.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)

        self._whatsapp.waterfallConfig = waterfall_config if waterfall_config else Waterfall().proto

    @property
    def proto(self) -> pb.Whatsapp:
        return self._whatsapp