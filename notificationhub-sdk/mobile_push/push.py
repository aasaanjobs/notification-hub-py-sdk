from typing import List
import json

from base import get_expiry, validate_template
from common import Waterfall
from proto import notification_hub_pb2 as pb


class Push:
    _default_expiry_offset = 7  # 7 Days

    def __init__(
            self,
            arn_endpoints: List[str],
            template: str,
            context: dict = None,
            waterfall_config: Waterfall = None,
            expiry: int = None
    ):
        """
        Initiates Push object
        """
        self._push = pb.Push()
        self.__set_arn_endpoints(arn_endpoints)

        validate_template(template)
        self._push.template = template

        self._push.context = json.dumps(context) if context else '{}'
        self._push.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)
        self._push.waterfallConfig = waterfall_config if waterfall_config else Waterfall().proto

    def __set_arn_endpoints(self, arn_endpoints: List[str]):
        for _ in arn_endpoints:
            self._push.arnEndpoints.append(_)

    @property
    def proto(self) -> pb.Push:
        return self._push
