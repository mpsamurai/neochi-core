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
            
class TestStartedIrRecevingNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StartedIrRecevingNotification
    valid_test_data = [{'published': 1, 'subscribed': 1}]
    
class TestStoppedIrReceivingNoSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingNoSignalNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedIrReceivingInvalidSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingInvalidSignalNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedIrReceivingValidSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingValidSignalNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedIrReceivingStopMessageNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingStopMessageNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedIrReceivingMoreSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrReceivingMoreSignalNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedIrSavingNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrSavingNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedIrSavingErrorNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedIrSavingErrorNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStoppedDiscardingNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedDiscardingNotification
    valid_test_data = [{'published': None, 'subscribed': None}]

class TestStoppedDiscardingErrorNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StoppedDiscardingErrorNotification
    valid_test_data = [{'published': 'Discarding error occurred', 'subscribed': 'Discarding error occurred'}]
    
class TestStartIrReceivingNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StartIrReceivingNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestStopIrReceivingNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.StopIrReceivingNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestSaveIrSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.SaveIrSignalNotification
    valid_test_data = [{'published': '0,TV Remote,500', 'subscribed': '0,TV Remote,500'}]
    
class TestDiscardIrSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.DiscardIrSignalNotification
    valid_test_data = [{'published': None, 'subscribed': None}]
    
class TestDeleteIrSignalNotification(BaseTestNotification, unittest.TestCase):
    notification_cls = ir_receiver.DeleteIrSignalNotification
    valid_test_data = [{'published': '0', 'subscribed': '0'}]