import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/matthew/asup/'
hostname= 'test2'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['POST'])
def upload_file():
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            if   os.path.isdir(UPLOAD_FOLDER+hostname) == True:  
                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], hostname ,filename))
                 return "File %s has been uploaded" % filename 
            else: 
                 os.mkdir(UPLOAD_FOLDER+hostname)
                 return "Welcome New Customer we see this is the first time you are using the autosupport tool since your hostname is not in use withen our system."
                 return "path is created"
app.route('/', methods=['GET'])
def welcome():
    return "Asup API V0.0.2"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

