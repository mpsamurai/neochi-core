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
import json
import numpy as np
import base64


class BaseDataType:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = self._decode(val)

    def to_string(self):
        return self._encode(self._value)
    
    def _encode(self, value):
        raise NotImplementedError

    def _decode(self, value):
        raise NotImplementedError


class Null(BaseDataType):
    def __init__(self):
        super().__init__()
        self._value = None

    def _encode(self, value):
        return str(None)

    def _decode(self, value):
        return None


class AtomicDataType(BaseDataType):
    type = None

    def _encode(self, value):
        return str(value)

    def _decode(self, value):
        if isinstance(value, bytes) and self.type != bytes:
            return self.type(value.decode())
        else:
            return value


class Int(AtomicDataType):
    type = int


class Float(AtomicDataType):
    type = float


class Str(AtomicDataType):
    type = str


class Datetime(BaseDataType):
    format = '%Y%m%d%H%M%S%f'

    def _encode(self, value):
        return value.strftime(self.format)

    def _decode(self, value):
        if isinstance(value, bytes):
            return datetime.strptime(value.decode(), self.format)
        else:
            return value


class Json(BaseDataType):
    def _encode(self, value):
        return json.dumps(value)

    def _decode(self, value):
        if isinstance(value, bytes):
            value = value.decode()
            return json.loads(value)
        return value


class NDArray(Json):
    def _encode(self, value):
        value = value.tolist()
        return json.dumps(value)

    def _decode(self, value):
        if isinstance(value, bytes):
            value = value.decode()
            return np.array(json.loads(value))
        return value


class Image(BaseDataType):
    datetime_format = '%Y%m%d%H%M%S%f'

    def _encode(self, value):
        image = base64.b64encode(value.tostring()).decode()
        now = datetime.now()
        return json.dumps({'width': value.shape[1], 
                           'height': value.shape[0], 
                           'channel': value.shape[2], 
                           'timeStamp': now.strftime(self.datetime_format),
                           'image': image})

    def _decode(self, value):
        if isinstance(value, bytes):
            value = value.decode()
            value = json.loads(value)
            buf = base64.b64decode(value['image'].encode())
            return np.frombuffer(buf, dtype=np.uint8).reshape((value['height'], value['width'], value['channel']))
        if isinstance(value, list):
            return np.array(value, dtype=np.uint8)
        return value
