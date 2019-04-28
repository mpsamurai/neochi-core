import time
import cv2
try:
    PI_CAMERA = True
    from picamera.array import PiRGBArray
    from picamera import PiCamera
except ImportError:
    PI_CAMERA = False
from neochi.neochi import settings
from neochi.eye import caches


class Capture:
    def __init__(self, cache_server, shape, rotation):
        self._state = cache_server.state
        self._image = cache_server.image
        self._shape = shape
        self._rotation = rotation
        self._frame = None

    @property
    def state(self):
        return self._state.get()

    @property
    def image(self):
        return self._state.get()

    def capture(self):
        ret, frame = self._capture()
        self.cache()
        return ret, frame

    def _capture(self):
        raise NotImplementedError

    def cache(self):
        if self._frame is not None:
            self._image.set(self._frame)


class CvCapture(Capture):
    def __init__(self, cache_server, shape, rotation):
        super().__init__(cache_server, shape, rotation)
        self._cap = cv2.VideoCapture(0)

    def _capture(self):
        ret, frame = self._cap.read()
        if ret and frame is not None:
            self._frame = cv2.cvtColor(cv2.resize(frame, tuple(self._shape)), cv2.COLOR_BGR2RGB)
        return ret, frame

    def release(self):
        self._cap.release()


class PiCapture(Capture):
    def __init__(self, cache_server, shape, rotation):
        super().__init__(cache_server, shape, rotation)
        self._camera = PiCamera(resolution=shape)
        self._camera.rotation = self._rotation
        self._cap = PiRGBArray(self._camera)

    def _capture(self):
        self._camera.capture(self._cap, format='rgb', use_video_port=True)
        frame = self._cap.array
        if frame.shape is None:
            return False, frame
        self._cap.truncate(0)
        self._frame = frame
        return True, self._frame

    def release(self):
        self._camera.close()


def start_capture():
    print('START CAPTURE.')
    if not PI_CAMERA:
        cap = CvCapture(caches.server, settings.eye_settings.get()['shape'], 0)
    else:
        cap = PiCapture(caches.server, settings.eye_settings.get()['shape'], 90)
    while True:
        cap.capture()
        time.sleep(1. / settings.eye_settings.get()['fps'])


if __name__ == '__main__':
    start_capture()