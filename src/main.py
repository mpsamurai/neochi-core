from neochi.core.dataflow.data import kinesis
import redis
import json

if __name__ == '__main__':
    r = redis.StrictRedis('redis', 6379, db=0)
    kinesis_action_plan = kinesis.ActionPlan(r)
    sample_data = {
        'detected_sleep': 0, 
        'detected_clap': 1
    }

    kinesis_action_plan.value = sample_data
    print(r.get('kinesis:action-plan'))

    sample_data['detected_sleep'] = 1
    r.set('kinesis:action-plan', json.dumps(sample_data))
    print(kinesis_action_plan)
