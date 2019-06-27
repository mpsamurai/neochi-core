import os

REDIS_HOST = os.environ.get('NEOCHI_REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('NEOCHI_REDIS_PORT', '6379'))

EYE_CAP_SIZE = (int(os.environ.get('NEOCHI_EYE_CAP_WIDTH', '32')), int(os.environ.get('EYE_CAP_HEIGHT', '32')))
EYE_CAP_FPS = os.environ.get(float(os.environ.get('NEOCHI_EYE_CAP_FPS', '0.5')))