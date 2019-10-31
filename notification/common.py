import protocol.notification_hub_pb2 as pb
from enum import IntFlag


class MessageType(IntFlag):
    MARKETING = 0
    TRANSACTIONAL = 1

class WaterfallMode(IntFlag):
    AUTO = 0
    OVERRIDE = 1

class Waterfall:
    """
    Initiates Waterfall object
    The priority of the channel in the task
    The time offset in seconds after which the notification should be triggered after the previous channel
    """
    def __init__(self, priority : int = 0, offset_time: int = 0):

        self._waterfall = pb.Waterfall()
        self._waterfall.priority = priority
        self._waterfall.offsetTime = offset_time

    def set_priority(self, priority : int):
        """
        Sets priority of the channel in the task

        Parameter:
            int

        :return:
            None
        """
        self._waterfall.priority = priority

    def get_priority(self) -> int:
        return self._waterfall.priority

    def del_priority(self):
        del self._waterfall.priority

    def set_offset_time(self, offset_time):
        """
        Sets time offset in seconds after which the notification should be triggered after the previous channel

        Parameter:
            int

        :return:
            None
        """
        self._waterfall.offsetTime = offset_time

    def get_offset_time(self) -> int:
        self._waterfall.offsetTime

    def del_offset_time(self):
        del self._waterfall.offsetTime

    def __str__(self):
        return f'priority: {self._waterfall.priority}, offset_time: {self._waterfall.offset_time}'

    def __repr__(self):
        return f'{self._waterfall.priority}, {self._waterfall.offset_time}'

    def get_object(self):
        """
        :return:
            Waterfall protobuf object
        """
        return self._waterfall

