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


class StartedIrRecevingNotification(base.BaseNotification):
    data_type_cls = data_types.Int
    channel = 'started_ir_receiving'
    
class StoppedIrReceivingNoSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_no_signal'
    
class StoppedIrReceivingInvalidSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_invalid_signal'
    
class StoppedIrReceivingValidSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_valid_signal'
    
class StoppedIrReceivingStopMessageNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_stop_message'
    
class StoppedIrReceivingMoreSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_receiving_more_signal'
    
class StoppedIrSavingNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_saving'
    
class StoppedIrSavingErrorNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_ir_saving_error'
    
class StoppedDiscardingNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stopped_discarding'
    
class StoppedDiscardingErrorNotification(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'stopped_discarding_error'
    
class StartIrReceivingNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'start_ir_receiving'
    
class StopIrReceivingNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'stop_ir_receiving'
    
class SaveIrSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'save_ir_signal'
    
class DiscardIrSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Null
    channel = 'discard_ir_signal'
    
class DeleteIrSignalNotification(base.BaseNotification):
    data_type_cls = data_types.Str
    channel = 'delete_ir_signal'