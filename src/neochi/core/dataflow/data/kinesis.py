from neochi.core.dataflow.data import base
from neochi.core.dataflow import data_types

class ActionPlan(base.BaseData):
    data_type_cls = data_types.Json
    key = 'kinesis:action-plan'
