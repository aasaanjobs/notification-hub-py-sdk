from typing import List
import json

from ..base import get_expiry, validate_template, validate_arn_endpoint
from ..common import Waterfall
from ..proto import notification_hub_pb2 as pb


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

        for _ in arn_endpoints:
            validate_arn_endpoint(_)
        self.__set_arn_endpoints(arn_endpoints)

        validate_template(template)
        self._push.template = template

        self._push.context = json.dumps(context) if context else '{}'
        self._push.expiry = expiry if expiry else get_expiry(self._default_expiry_offset)
        self.__set_waterfall(waterfall_config)

    def __set_arn_endpoints(self, arn_endpoints: List[str]):
        for _ in arn_endpoints:
            self._push.arnEndpoints.append(_)

    def __set_waterfall(self, value: Waterfall = None):
        if not value:
            value = Waterfall()
        self._push.waterfallConfig.CopyFrom(value.proto)

    @property
    def proto(self) -> pb.Push:
        return self._push
