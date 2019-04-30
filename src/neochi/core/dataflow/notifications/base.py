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


class ChannelIsAlreadySubscribed(Exception):
    pass


class BaseNotification:
    data_type_cls = None
    channel = ''

    def __init__(self, redis_server, auto_notify=True):
        self._server = redis_server
        self._data = self.data_type_cls()
        self._pubsub = None
        self.auto_notify = auto_notify
        self._subscribe_thread = None

    def _subscribe(self, callback):
        for message in self._pubsub.listen():
            if message['type'] == 'message':
                self._data.value = message['data']
                if callback is not None:
                    callback(self._data.value, self.channel)
        self._subscribe_thread = None

    def subscribe(self, callback=None):
        if self._pubsub is None:
            self._pubsub = self._server.pubsub()
        if self._subscribe_thread is not None:
            raise ChannelIsAlreadySubscribed
        self._pubsub.subscribe(self.channel)
        self._subscribe_thread = threading.Thread(target=self._subscribe, args=([callback, ]))
        self._subscribe_thread.start()

    def wait_subscription_end(self):
        self._subscribe_thread.join()

    def unsubscribe(self):
        self._pubsub.unsubscribe(self.channel)

    def notify(self):
        self._server.publish(self.channel, self._data.to_string())

    @property
    def value(self):
        return self._data.value

    @value.setter
    def value(self, val):
        self._data.value = val
        if self.auto_notify:
            self.notify()
