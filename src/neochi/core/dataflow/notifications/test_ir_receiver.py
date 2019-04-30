import time
import redis
import unittest
import numpy as np
from neochi.core.dataflow import data_types
from neochi.core.dataflow.notifications import base
from neochi.core.dataflow.notifications import ir_receiver


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


class TestStartedIrReceving(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StartedIrReceving
    valid_test_data = [{'published': 1, 'subscribed': 1}]


class TestStoppedIrReceivingNoSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingNoSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingInvalidSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingInvalidSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingValidSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingValidSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingStopMessage(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingStopMessage
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingMoreSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingMoreSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrSaving(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrSaving
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrSavingError(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrSavingError
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedDiscarding(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedDiscarding
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedDiscardingError(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedDiscardingError
    valid_test_data = [{'published': 'Discarding error occurred', 'subscribed': 'Discarding error occurred'}]


class TestStartIrReceiving(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StartIrReceiving
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStopIrReceiving(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StopIrReceiving
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestSaveIrSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.SaveIrSignal
    valid_test_data = [{'published': '0,TV Remote,500', 'subscribed': '0,TV Remote,500'}]


class TestDiscardIrSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.DiscardIrSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestDeleteIrSignal(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.DeleteIrSignal
    valid_test_data = [{'published': '0', 'subscribed': '0'}]