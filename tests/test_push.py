import unittest

from notificationhub_sdk.common import Waterfall
from notificationhub_sdk.base import InvalidArnEndpoint, InvalidTemplateURL
from notificationhub_sdk.mobile_push import Push


class TestPush(unittest.TestCase):
    def setUp(self) -> None:
        self.correct_arn_endpoint = 'arn:aws:iam::123456789012:user/Development/product_1234/*'
        self.correct_template = 'https://static.aasaanjobs.com/push_template.html'
        self.incorrect_arn_endpoint = 'abcdef'
        self.incorrect_template = 'push_template.html'

    def test_correct_arn(self):
        obj = Push(arn_endpoints=[self.correct_arn_endpoint], template=self.correct_template)
        self.assertEqual(obj.proto.arnEndpoints[0], self.correct_arn_endpoint)

    def test_incorrect_arn(self):
        with self.assertRaises(InvalidArnEndpoint):
            Push(arn_endpoints=[self.incorrect_arn_endpoint], template=self.correct_template)

    def test_correct_template(self):
        obj = Push(arn_endpoints=[self.correct_arn_endpoint], template=self.correct_template)
        self.assertEqual(obj.proto.template, self.correct_template)

    def test_incorrect_template(self):
        with self.assertRaises(InvalidTemplateURL):
            Push(arn_endpoints=[self.correct_arn_endpoint], template=self.incorrect_template)

    def test_waterfall(self):
        obj = Push(arn_endpoints=[self.correct_arn_endpoint], template=self.correct_template,
                   waterfall_config=Waterfall(priority=1, offset_time=60))
        self.assertEqual(obj.proto.waterfallConfig.priority, 1)
        self.assertEqual(obj.proto.waterfallConfig.offsetTime, 60)
