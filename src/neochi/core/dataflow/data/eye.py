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

from neochi.core.dataflow.data import base
from neochi.core.dataflow import data_types


class Image(base.BaseData):
    data_type_cls = data_types.Image
    key = 'image'


class State(base.BaseData):
    data_type_cls = data_types.Json
    key = 'state'


if __name__ == "__main__":
    # Local var
    fps = 2 

    # RedisとのConnect
    r = redis.StrictRedis("redis", 6379, db=0)
    eye_image = Image(r)
    eye_state = State(r)

    while True:
        # Receive
        image_size_dict = json.loads(eye_state.value)

        width = image_size_dict["image_size"]["width"]
        height = image_size_dict["image_size"]["height"]
        image_size = [width, height]

        # Get Image
        _, captured_image = get_image.start_capture(image_size)

        # Transmit
        eye_image.value = captured_image

        time.sleep(1. /fps)   
