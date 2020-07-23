import json
from flask import Flask, flash, request, redirect, send_file, render_template
from predict import predict_results

app = Flask(__name__, template_folder='templates')

with open('cat_to_name.json', 'r') as f:
    flowers_map = json.load(f)

flowers = sorted(list(flowers_map.values()))


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file sent.'
        results = predict_results(request.files["file"])
        return render_template('predictions.html', results=results)


@app.route('/', methods=['GET'])
def index():
    return render_template('landing.html', flowers=flowers)
