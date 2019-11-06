import unittest

from notificationhub_sdk.common import Waterfall
from notificationhub_sdk.base import InvalidMobile, InvalidTemplateURL
from notificationhub_sdk.whatsapp import Whatsapp


class TestWhatsapp(unittest.TestCase):
    def setUp(self) -> None:
        self.correct_mobile = '8698009019'
        self.correct_template = 'https://static.aasaanjobs.com/whatsapp_template.html'
        self.incorrect_mobile = '21234'
        self.incorrect_template = 'whatsapp_template.html'

    def test_correct_mobile(self):
        obj = Whatsapp(send_to=self.correct_mobile, template=self.correct_template)
        self.assertEqual(obj.proto.mobile, self.correct_mobile)

    def test_incorrect_mobile(self):
        with self.assertRaises(InvalidMobile):
            Whatsapp(send_to=self.incorrect_mobile, template=self.correct_template)

    def test_correct_template(self):
        obj = Whatsapp(send_to=self.correct_mobile, template=self.correct_template)
        self.assertEqual(obj.proto.template, self.correct_template)

    def test_incorrect_template(self):
        with self.assertRaises(InvalidTemplateURL):
            Whatsapp(send_to=self.correct_mobile, template=self.incorrect_template)

    def test_waterfall(self):
        obj = Whatsapp(send_to=self.correct_mobile, template=self.correct_template,
                       waterfall_config=Waterfall(priority=1, offset_time=60))
        self.assertEqual(obj.proto.waterfallConfig.priority, 1)
        self.assertEqual(obj.proto.waterfallConfig.offsetTime, 60)
