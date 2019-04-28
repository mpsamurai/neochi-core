import os
import pickle
from neochi.core import caches


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, '../../data')
MODEL_DIR = os.path.join(BASE_DIR, '../../models')


EYE = {
    'capture': {
        'cache_host': 'localhost',
        'cache_port': 6379,
        'fps': 5,
        'shape': (64, 64)
    }
}


BRAIN = {
    'detectors': {
        'person_detector': {
            'model': {
                'image_shape': [64, 64],
                'save_path': os.path.join(MODEL_DIR, 'person_detector/mlp.pickle'),
            },
            'ma': {
                'n': 20,
                'initial_value': 0.5,
                'save_path': os.path.join(MODEL_DIR, 'person_detector/ma.pickle'),
            },
            'executor': {
                'fps': 5,
                'save_path': os.path.join(MODEL_DIR, 'person_detector/executor.pickle'),
            },
            'cache_host': 'localhost',
            'cache_port': 6379,
        },
        'movement_detector': {
            'model': {
                'cutoff': 180,
                'detection_threshold': 10,
                'save_path': os.path.join(MODEL_DIR, 'movement_detector/model.pickle'),
            },
            'ma': {
                'n': 20,
                'initial_value': 1.0,
                'save_path': os.path.join(MODEL_DIR, 'movement_detector/ma.pickle'),
            },
            'executor': {
                'lay_down_threshold': 0.9,
                'fps': 5,
                'save_path': os.path.join(MODEL_DIR, 'movement_detector/executor.pickle'),
            },
            'cache_host': 'localhost',
            'cache_port': 6379,
        },
        'sleep_detector': {
            'model': {
                'history_length': 20,
                'detection_threshold': 0.5,
                'save_path': os.path.join(MODEL_DIR, 'sleep_detector/model.pickle'),
            },
            'ma': {
                'n': 40,
                'initial_value': 0.,
                'save_path': os.path.join(MODEL_DIR, 'sleep_detector/ma.pickle'),
            },
            'executor': {
                'lay_down_threshold': 0.9,
                'history_length': 20,
                'fps': 5,
                'save_path': os.path.join(MODEL_DIR, 'sleep_detector/executor.pickle'),
            },
            'cache_host': 'localhost',
            'cache_port': 6379,
        },
        'clap_detector': {
            'expires': 1,
        }
    }
}


KINESIS = {
    'mabeee': {
        'sleep_detection_threshold': 0.9,
        'host': '192.168.1.98',
        'port': 8080,
        'fps': 1,
    }
}


WEB = {
    'templates_dir': os.path.join(BASE_DIR, 'web/templates'),
    'streaming': {
        'image_shape': [64, 64]
    },
    'training': {
        'lock': os.path.join(BASE_DIR, 'web/lock_train'),
        'script': 'python3 %s execute-train' % os.path.join(BASE_DIR, 'brain/detectors.py')
    }
}


class EyeSettings(caches.JsonCache):
    KEY = 'neochi_eye_captures_settings'


class PersonDetectorSettings(caches.JsonCache):
    KEY = 'neochi_brain_detectors_person_detector_settings'


class MovingDetectorSettings(caches.JsonCache):
    KEY = 'neochi_brain_detectors_movement_detector_settings'


class SleepDetectorSettings(caches.JsonCache):
    KEY = 'neochi_brain_detectors_sleep_detector_settings'


class MabeeeSettings(caches.JsonCache):
    KEY = 'neochi_kinesis_mabeee_settings'


class WebSettings(caches.JsonCache):
    KEY = 'neochi_web_settings'


class CacheServer(caches.CacheServer):
    CACHE_CLASSES = [EyeSettings,
                     PersonDetectorSettings,
                     MovingDetectorSettings,
                     SleepDetectorSettings,
                     MabeeeSettings,
                     WebSettings, ]


server = CacheServer()

eye_settings = server.eye_settings
# if eye_settings.get() is None:
eye_settings.set(EYE['capture'])

person_detector_settings = server.person_detector_settings
# if person_detector_settings.get() is None:
person_detector_settings.set(BRAIN['detectors']['person_detector'])

movement_detector_settings = server.moving_detector_settings
# if movement_detector_settings.get() is None:
movement_detector_settings.set(BRAIN['detectors']['movement_detector'])

sleep_detector_settings = server.sleep_detector_settings
# if sleep_detector_settings.get() is None:
sleep_detector_settings.set(BRAIN['detectors']['sleep_detector'])

mabeee_settings = server.mabeee_settings
# if mabeee_settings.get() is None:
mabeee_settings.set(KINESIS['mabeee'])

web_settings = server.web_settings
if web_settings.get() is None:
    web_settings.set(WEB)


print('EYE SETTINGS:')
print(eye_settings.get())
print()

print('PERSON DETECTOR SETTINGS:')
print(person_detector_settings.get())
print()

print('MOVEMENT DETECTOR SETTINGS:')
print(movement_detector_settings.get())
# save_path = movement_detector_settings.get()['save_path']
# if os.path.exists(save_path):
#     print('MOVEMENT DETECTOR SETTINGS UPDATED.')
#     with open(save_path, 'rb') as f:
#         movement_detector_settings.update({'model': pickle.load(f)})
print()

print('SLEEP DETECTOR SETTINGS:')
print(sleep_detector_settings.get())
# save_path = sleep_detector_settings.get()['save_path']
# if os.path.exists(save_path):
#     print('SLEEP DETECTOR SETTINGS UPDATED.')
#     with open(save_path, 'rb') as f:
#         sleep_detector_settings.update({'model': pickle.load(f)})
print()

print('MABEE SETTINGS')
print(mabeee_settings.get())
print()

print('WEB SETTINGS')
print(web_settings.get())
print()