from neochi.core.dataflow.notifications import BaseNotification
import redis
import numpy as np
import threading
from neochi.core.dataflow import data_types

class ClapDetectorNotification(BaseNotification):
    data_type_cls = data_types.Str
    channel = 'clap-detector:state'

r = redis.StrictRedis('127.0.0.1', 6739, db=0)
clap_detector_notification = ClapDetectorNotification(r)
clap_detector_notification.subscribe(callback)
clap_detector_notification.value='booting'
clap_detector_notification.subscribe(callback)
clap_detector_notification.value='ready'
clap_detector_notification.subscribe(callback)
clap_detector_notification.value='dead'
clap_detector_notification.subscribe(callback)



