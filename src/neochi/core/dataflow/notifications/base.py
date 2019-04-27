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

import threading
from neochi.core.dataflow import data_types


class BaseNotification:
    data_type_cls = None
    channel = ''

    def __init__(self, redis_server):
        self._server = redis_server
        self._data_type = self.data_type_cls()
        self._pubsub = None
        self._subscribe_thread = None

    def _subscribe(self, callback):
        for message in self._pubsub.listen():
            if message['type'] == 'message':
                self._data_type.value = message['data']
                callback(self._data_type.value)
        print('unsubscribed')

    def subscribe(self, callback):
        if self._pubsub is None:
            self._pubsub = self._server.pubsub()
        self._pubsub.subscribe(self.channel)
        self._subscribe_thread = threading.Thread(target=self._subscribe, args=([callback, ]))
        self._subscribe_thread.start()

    def unsubscribe(self):
        self._pubsub.unsubscribe(self.channel)

    @property
    def value(self):
        return self._data_type.value

    @value.setter
    def value(self, val):
        self._data_type.value = val
        self._server.publish(self.channel, self._data_type.to_string())


if __name__ == '__main__':
    import redis
    import numpy as np

    class SampleImageNotification(BaseNotification):
        data_type_cls = data_types.Image
        channel = 'sample_image_data'

    class SampleJsonNotification(BaseNotification):
        data_type_cls = data_types.Json
        channel = 'sample_json_data'

    def callback(value):
        print(value)

    r = redis.StrictRedis('localhost', 6379, db=0)
    image_notification = SampleImageNotification(r)
    image_notification.subscribe(callback)
    image_notification.value = np.array([[1, 2], [1, 3]])
    image_notification.value = np.array([[2, 2], [1, 3]])
    image_notification.value = np.array([[3, 2], [1, 3]])
    image_notification.unsubscribe()
    print('last-result\n', image_notification.value)

    json_notification = SampleJsonNotification(r)
    json_notification.subscribe(callback)
    json_notification.value = {'abc': 1, 'cde': 'abc'}
    json_notification.unsubscribe()
    json_notification.value = {'cde': 2, 'efg': 'abc'}
    print('last-result\n', json_notification.value)
