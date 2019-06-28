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


__author__ = 'Junya Kaneko <junya@mpsamurai.org>'


import time
from .. import data


class DataReceiver:
    data_class = data.base.BaseData

    def __init__(self, redis_server, fps):
        self._data = self.data_class(redis_server)
        self._fps = fps
        self.quit = False

    def receive(self):
        last_time = None
        while True:
            if self.quit:
                break
            if last_time is not None and 1. / self._fps - (time.time() - last_time) > 0:
                yield False, None
                continue
            last_time = time.time()
            yield True, self._data.value


class SequentialDataReceiver(DataReceiver):
    data_class = data.base.BaseData

    def __init__(self, redis_server, fps, length):
        super().__init__(redis_server, fps)
        self._length = length

    def receive(self):
        last_time = None
        data_seq = []
        while True:
            if self.quit:
                break
            if last_time is not None:
                sleep_duration = 1. / self._fps - (time.time() - last_time) > 0
                if sleep_duration > 0:
                    time.sleep(sleep_duration)
            last_time = time.time()
            data_seq.append(self._data.value)
            if len(data_seq) < self._length:
                yield False, None
                continue
            elif len(data_seq) > self._length:
                data_seq = data_seq[1:]
            yield True, data_seq
