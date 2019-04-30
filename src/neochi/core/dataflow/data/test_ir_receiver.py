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


import redis
import unittest
import numpy as np
from neochi.core.dataflow import data_types
from neochi.core.dataflow.data import base
from neochi.core.dataflow.data import ir_receiver


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


class TestState(BaseTestData, unittest.TestCase):
    data_cls = ir_receiver.State
    valid_test_data = [
        {'value_set': 'booting', 'value_got': 'booting', 'value_in_redis': b'booting'}
    ]


class TestIr(BaseTestData, unittest.TestCase):
    data_cls = ir_receiver.Ir
    valid_test_data = [
            {'value_set':        {'signals': [{'id': 0, 
                                                'name': 'TV Remote ON', 
                                                'sleep': 500, 
                                                'filePath': '/home/neochi/0.ir', 
                                                'fileTimeStamp': '20190101'}]},
             'value_got':        {'signals': [{'id': 0, 
                                                'name': 'TV Remote ON', 
                                                'sleep': 500, 
                                                'filePath': '/home/neochi/0.ir', 
                                                'fileTimeStamp': '20190101'}]},
             'value_in_redis': b'{"signals": [{"id": 0, ' +
                                                b'"name": "TV Remote ON", ' +
                                                b'"sleep": 500, ' +
                                                b'"filePath": "/home/neochi/0.ir", ' +
                                                b'"fileTimeStamp": "20190101"}]}'}
            ]