import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/matthew/asup/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file :
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "File %s has been uploaded"%  filename

@app.route('/', methods=['GET'])
def welcome():
    return "Asup API V0.0.2"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

