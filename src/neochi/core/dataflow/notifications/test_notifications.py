# MIT License
#
# Copyright (c) 2019 Morning Project Samurai (MPS)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__author__ = 'Junya Kaneko<junya@mpsamurai.org>'

import time
import redis
import unittest
import numpy as np
from neochi.core.dataflow import data_types
from neochi.core.dataflow.notifications import base


class NullTestNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'null_test_notification'


class IntTestNotification(base.BaseNotification):
    data_type_cls = data_types.Int
    channel = 'int_test_notification'


class FloatTestNotification(base.BaseNotification):
    data_type_cls = data_types.Float
    channel = 'float_test_notification'


class StrTestNotification(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'str_test_notification'


class JsonTestNotification(base.BaseNotification):
    data_type_cls = data_types.Json
    channel = 'json_test_notification'


class ImageTestNotification(base.BaseNotification):
    data_type_cls = data_types.Image
    channel = 'image_test_notification'


class BaseTestNotification:
    notification_cls = base.BaseNotification
    valid_test_data = []

    def setUp(self):
        self._r = redis.StrictRedis('redis')
        self._notification = self.notification_cls(self._r)

    def test_that_setter_and_getter_value_pubsubs_valid_data_when_valid_data_is_given(self):
        for datum in self.valid_test_data:
            self._notification.subscribe(lambda v: self.assertEqual(v, datum['subscribed']))
            self._notification.value = datum['published']
            time.sleep(0.1)
            self._notification.unsubscribe()


class TestNullTestNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = NullTestNotification
    valid_test_data = [{'published': 'abc', 'subscribed': None}]


class TestIntTestNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = IntTestNotification
    valid_test_data = [{'published': 1, 'subscribed': 1}]


class TestFloatTestNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = FloatTestNotification
    valid_test_data = [{'published': 1.0, 'subscribed': 1.0}]


class TestStrTestNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = StrTestNotification
    valid_test_data = [{'published': 'abc', 'subscribed': 'abc'}]


class TestJasonTestNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = JsonTestNotification
    valid_test_data = [{'published': {'abc': 1}, 'subscribed': {'abc': 1}}]


class TestImageTestNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ImageTestNotification
    valid_test_data = [{'published': np.array([[1, 2], [3, 4]]),
                        'subscribed': np.array([[1, 2], [3, 4]])}]

    def test_that_setter_and_getter_value_pubsubs_valid_data_when_valid_data_is_given(self):
        for datum in self.valid_test_data:
            self._notification.subscribe(lambda v: self.assertTrue(np.all(v == datum['subscribed'])))
            self._notification.value = datum['published']
            time.sleep(0.1)
            self._notification.unsubscribe()

