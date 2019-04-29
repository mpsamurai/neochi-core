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


from datetime import datetime
import redis
import unittest
import numpy as np
from neochi.core.dataflow import data_types
from neochi.core.dataflow.data import base


class NullTestData(base.BaseData):
    data_type_cls = data_types.Null
    key = 'null_test_data'


class IntTestData(base.BaseData):
    data_type_cls = data_types.Int
    key = 'int_test_data'


class FloatTestData(base.BaseData):
    data_type_cls = data_types.Float
    key = 'float_test_data'


class StrTestData(base.BaseData):
    data_type_cls = data_types.Str
    key = 'str_test_data'


class DatetimeTestData(base.BaseData):
    data_type_cls = data_types.Datetime
    key = 'datetime_test_data'


class JsonTestData(base.BaseData):
    data_type_cls = data_types.Json
    key = 'json_test_data'


class ImageTestData(base.BaseData):
    data_type_cls = data_types.Image
    key = 'image_test_data'


class BaseTestData:
    data_cls = base.BaseData
    valid_test_data = []

    def setUp(self):
        self._r = redis.StrictRedis('redis')
        if self._r.exists(self.data_cls.key):
            self._r.delete(self.data_cls.key)
        self._data = self.data_cls(self._r)

    def test_that_setter_value_sets_valid_data_to_redis_when_valid_data_is_given(self):
        for datum in self.valid_test_data:
            self._data.value = datum['value_set']
            assert self._r.get(self._data.key) == datum['value_in_redis']

    def test_that_getter_value_gets_valid_data_from_redis_when_valid_data_is_given(self):
        for datum in self.valid_test_data:
            self._r.set(self._data.key, datum['value_in_redis'])
            assert self._data.value == datum['value_got']

    def tearDown(self):
        self._r.delete(self.data_cls.key)
        self._data = None


class TestNullTestData(BaseTestData, unittest.TestCase):
    data_cls = NullTestData
    valid_test_data = [
        {'value_set': 'abc', 'value_got': None, 'value_in_redis': b'None'},
    ]


class TestIntTestData(BaseTestData, unittest.TestCase):
    data_cls = IntTestData
    valid_test_data = [
        {'value_set': 1, 'value_got': 1, 'value_in_redis': b'1'}
    ]


class TestFloatTestData(BaseTestData, unittest.TestCase):
    data_cls = FloatTestData
    valid_test_data = [
        {'value_set': 0.1, 'value_got': 0.1, 'value_in_redis': b'0.1'}
    ]


class TestStrTestData(BaseTestData, unittest.TestCase):
    data_cls = StrTestData
    valid_test_data = [
        {'value_set': 'abc', 'value_got': 'abc', 'value_in_redis': b'abc'}
    ]


class TestDatetimeTestData(BaseTestData, unittest.TestCase):
    data_cls = DatetimeTestData
    valid_test_data = [
        {'value_set': datetime(2019, 4, 27),
         'value_got': datetime(2019, 4, 27),
         'value_in_redis': datetime(2019, 4, 27).strftime(DatetimeTestData.data_type_cls.format).encode()}
    ]


class TestJsonTestData(BaseTestData, unittest.TestCase):
    data_cls = JsonTestData
    valid_test_data = [
        {'value_set': {'int': 1, 'str': 'abc'},
         'value_got': {'int': 1, 'str': 'abc'},
         'value_in_redis': b'{"int": 1, "str": "abc"}'}
    ]


class TestImageTestData(BaseTestData, unittest.TestCase):
    data_cls = ImageTestData
    valid_test_data = [
        {'value_set': np.array([[1, 2], [1, 3]]),
         'value_got': np.array([[1, 2], [1, 3]]),
         'value_in_redis': b'{"shape": [2, 2], ' +
                           b'"image": "\u0001\u0000\u0000\u0000\u0002\u0000\u0000' +
                           b'\u0000\u0001\u0000\u0000\u0000\u0003\u0000\u0000\u0000"}'},
    ]

    def test_that_getter_value_gets_valid_data_from_redis_when_valid_data_is_given(self):
        for datum in self.valid_test_data:
            self._r.set(self._data.key, datum['value_in_redis'])
            assert np.all(self._data.value == datum['value_got'])

