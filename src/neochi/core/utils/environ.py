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


import os
import json


class InvalidEnvironmentVariable(Exception):
    pass


def cast(type_str):
    if type_str == 'STR':
        return str
    elif type_str == 'INT':
        return int
    elif type_str == 'FLOAT':
        return float
    elif type_str == 'JSON':
        return json.loads
    else:
        raise InvalidEnvironmentVariable(type_str)


def get_kwargs(prefix):
    kwargs = {}
    for key in os.environ.keys():
        if not key.startswith('NEOCHI'):
            continue
        terms = key.split(':')
        if len(terms) < 4:
            raise InvalidEnvironmentVariable(key)
        if not terms[1].startswith(prefix):
            continue
        kwargs[terms[2].lower()] = cast(terms[3])(os.environ[key])
    return kwargs

