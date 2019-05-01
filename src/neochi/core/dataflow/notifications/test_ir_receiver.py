import time
import redis
import unittest
import numpy as np
from neochi.core.dataflow import data_types
from neochi.core.dataflow.notifications import test_base, ir_receiver


class TestStartedIrReceiving(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StartedIrReceiving
    valid_test_data = [{'published': 1, 'subscribed': 1}]


class TestStoppedIrReceivingNoSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingNoSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingInvalidSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingInvalidSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingValidSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingValidSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingStopMessage(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingStopMessage
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrReceivingMoreSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingMoreSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrSaving(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrSaving
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedIrSavingError(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrSavingError
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedDiscarding(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedDiscarding
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStoppedDiscardingError(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedDiscardingError
    valid_test_data = [{'published': 'Discarding error occurred', 'subscribed': 'Discarding error occurred'}]


class TestStartIrReceiving(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StartIrReceiving
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestStopIrReceiving(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StopIrReceiving
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestSaveIrSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.SaveIrSignal
    valid_test_data = [{'published': {'id': 0, 'name': 'TV Remote', 'sleep': 500}, 'subscribed': {'id': 0, 'name': 'TV Remote', 'sleep': 500}}]


class TestDiscardIrSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.DiscardIrSignal
    valid_test_data = [{'published': None, 'subscribed': None}]


class TestDeleteIrSignal(test_base.BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.DeleteIrSignal
    valid_test_data = [{'published': '0', 'subscribed': '0'}]