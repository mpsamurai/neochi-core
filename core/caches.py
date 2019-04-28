import copy
from datetime import datetime
import numpy as np
import redis
import json


class Cache:
    KEY = 'cache_key_name'
    TYPE = str

    def __init__(self, cache):
        self._cache = cache

    def set(self, value):
        self._cache.set(self.KEY, value)

    def get(self):
        value = self._cache.get(self.KEY)
        if value is None:
            return None
        elif self.TYPE != str:
            return self.TYPE(value)
        else:
            return value.decode()


class JsonCache(Cache):
    KEY = 'cache_key_name'

    def set(self, value):
        self._cache.set(self.KEY, json.dumps(value))

    def update(self, value):
        prev_value = self.get()
        updated_value = copy.deepcopy(prev_value)
        updated_value.update(value)
        if prev_value != updated_value:
            self.set(updated_value)
            return True
        else:
            return False

    def get(self):
        value = self._cache.get(self.KEY)
        if value is None:
            return {}
        return json.loads(value.decode())


class ImageCache:
    KEY = 'cache_key_name'

    @property
    def _name_key(self):
        return '%s_name' % self.KEY

    @property
    def _image_key(self):
        return '%s_image' % self.KEY

    @property
    def _height_key(self):
        return '%s_height' % self.KEY

    @property
    def _width_key(self):
        return '%s_width' % self.KEY

    @property
    def _channel_key(self):
        return '%s_channel' % self.KEY

    def __init__(self, cache):
        self._cache = cache

    def set(self, image, name=None):
        if name is None:
            name = '%s' % datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
        self._cache.set(self._name_key, name)
        self._cache.set(self._image_key, image.tostring())
        self._cache.set(self._height_key, image.shape[0])
        self._cache.set(self._width_key, image.shape[1])
        if len(image.shape) == 3:
            self._cache.set(self._channel_key, image.shape[2])

    def get(self):
        def get_shape():
            height = int(self._cache.get(self._height_key))
            width = int(self._cache.get(self._width_key))
            channel = int(self._cache.get(self._channel_key))
            if channel is not None:
                return height, width, channel
            else:
                return height, width
        return {'name': self._cache.get(self._name_key).decode(),
                'body': np.fromstring(self._cache.get(self._image_key),
                                      dtype=np.uint8).reshape(get_shape())}

    def get_name(self):
        return self.get()['name']

    def get_body(self):
        return self.get()['body']


class CacheServer:
    HOST = 'localhost'
    PORT = 6379

    CACHE_CLASSES = []

    _conn = None
    _instances = []

    def __init__(self):
        if self._conn is None:
            self._conn = redis.Redis(self.HOST, self.PORT)
        if not self._instances:
            self._instances = [cls(self._conn) for cls in self.CACHE_CLASSES]

    def __getattr__(self, item):
        cls_name = ''.join([word.title() for word in item.split('_')])
        for instance in self._instances:
            if instance.__class__.__name__ == cls_name:
                return instance
