import redis
import neochi.core

from flask import Flask, request, make_response, jsonify
import os
import werkzeug
from datetime import datetime

# host port set
HOSTIP = "0.0.0.0"
PORT=3001

# upload & download path set
UPLOAD_PATH = "/neochi/tmp/models/"
DOWNLOAD_PATH = "/neochi/models/"

# zipfile
zipfile = "model.zip"

# redis set
r = redis.StrictRedis('redis')

# flask set
app = Flask(__name__)

# post rollout
@app.route('/api/models', methods=['POST'])
def post():
	
	# set
    resultTrue  = { "Greeting Completed" : 'flask[POST] ok' }
    resultFalse = { "Greeting unCompleted": 'flask[POST] error' }
    
    #1 StartedModelUpload -> publish
    started_model_upload = notifications.brain_trained_model_uploader.StartedModelUpload(r)
    started_model_upload.notify()
    
    #2 State -> receiving
    State = data.brain_trained_model_uploader.State(r)
    State.value = "receiving"
    
    #3 unzip
    flg = unZip(zipfile, UPLOAD_PATH, DOWNLOAD_PATH)
    
    if flg:
		#4 LastUpdateTime -> publish
		LastUpdateTime = data.brain_trained_model_uploader.LastUpdateTime
		LastUpdateTime.value = datetime.now()
		
		#5 State -> ready
		State.value = "ready"
		
		#6 CompletedModelUpload -> publish
		completed_model_upload = nortifictions.brain_trained_model_uploader.CompletedModelUpload(r)
		completed_model_upload.notify()
		
		# success
		return make_response(jsonify(resultTrue))
	
	else:
		
		# roll back
		State = data.brain_trained_model_uploader.State(r)
        State.value = "ready"

		# unsuccess
		return make_response(jsonify(resultFalse))
		

# 400 error handling
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'400 error': 'Bad Request'}), 400)


# 403 error handling
@app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'403 error': 'Forbidden'}), 403)


# 404 error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'404 error': 'Not Found'}), 404)


# script run
# host = HOSTIP port = PORT
if __name__ == '__main__':
    api.run(host=HOSTIP, port=PORT)

