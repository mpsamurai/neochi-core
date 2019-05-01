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


from neochi.core.dataflow.notifications import base
from neochi.core.dataflow import data_types


class StartedIrReceiving(base.BaseNotification):
    data_type_cls = data_types.Int
    channel = 'started_ir_receiving'
    
    
class StoppedIrReceivingNoSignal(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_no_signal'
    
    
class StoppedIrReceivingInvalidSignal(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_invalid_signal'
    
    
class StoppedIrReceivingValidSignal(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_valid_signal'
    
    
class StoppedIrReceivingStopMessage(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_stop_message'
    
    
class StoppedIrReceivingMoreSignal(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_more_signal'
    
    
class StoppedIrSaving(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_saving'
    
    
class StoppedIrSavingError(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_saving_error'
    
    
class StoppedDiscarding(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_discarding'
    
    
class StoppedDiscardingError(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'stopped_discarding_error'
    
    
class StartIrReceiving(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'start_ir_receiving'
    
    
class StopIrReceiving(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stop_ir_receiving'
    
    
class SaveIrSignal(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'save_ir_signal'
    
    
class DiscardIrSignal(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'discard_ir_signal'
    
    
class DeleteIrSignal(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'delete_ir_signal'