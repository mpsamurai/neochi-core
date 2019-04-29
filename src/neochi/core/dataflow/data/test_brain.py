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
from neochi.core.dataflow.data import base, brain, test_base


class TestLyingPossibility(test_base.FloatTestData, unittest.TestCase):
    data_cls = brain.LyingPossibility
    valid_test_data = [
        {'value_set': 0.1, 'value_got': 0.1, 'value_in_redis': b'0.1'}
    ]

class TestIsMoving(test_base.IntTestData, unittest.TestCase):
    data_cls = brain.IsMoving
    valid_test_data = [
        {'value_set': 1, 'value_got': 1, 'value_in_redis': b'1'}
    ]


class TestSleepingPossibility(test_base.FloatTestData, unittest.TestCase):
    data_cls = brain.SleepingPossibility
    valid_test_data = [
        {'value_set': 0.1, 'value_got': 0.1, 'value_in_redis': b'0.1'}
    ]
