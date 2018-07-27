#!flask/bin/python
#Taken from:
# - https://stackoverflow.com/questions/28982974/flask-restful-upload-image
# - http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
import os
import json
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = 'uploaded-file' + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        return json.dumps({'filename':f_name})

@app.route('/')
def index():
    return "Hello world! Endpoints: [POST] /upload"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
