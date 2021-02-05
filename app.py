import json
from flask import Flask, flash, request, redirect, send_file, render_template, url_for
from predict import predict_results
from os import environ

app = Flask(__name__, template_folder='templates')
# Add this for max image size handling
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.secret_key = environ.get('secret')

# Image extensions recognized by PIL library. See https://pillow.readthedocs.io/en/5.1.x/handbook/image-file-formats.html
ALLOWED_EXTENSIONS = ['bmp', 'eps', 'jpg', 'gif', 'icns', 'ico','im', 'jpeg','msp','pcx','png','ppm','pgi','tiff','webp','xbm',
'blp', 'cur','dcx', 'fli', 'fpx', 'ftex','gbr','gd','imt','iptc','naa','mcidas','mic','mpo','pcd','pixar','psd','tga','wal','xpm']

#open mapping file species_number => species_name
with open('cat_to_name.json', 'r') as f:
    flowers_map = json.load(f)

flowers = sorted(list(flowers_map.values()))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files or request.files['file'].filename == '':
            flash('No file selected')
            return redirect("/")
        file = request.files['file']
        if file and allowed_file(file.filename):
            results = predict_results(request.files["file"])
            return render_template('predictions.html', results=results)
        flash("Can't read image type")
        return redirect("/")

@app.route('/', methods=['GET'])
def index():
    return render_template('landing.html', flowers=flowers)
