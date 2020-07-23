from flask import Flask,flash,request,redirect,send_file,render_template
app = Flask(__name__, template_folder='templates')
from predict import predict_results

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
      if 'file' not in request.files:
        return 'No file sent.'
      # predict_results('globe_thistle.jpg')
      return "Got File."

@app.route('/', methods=['GET'])
def index():
  return render_template('landing.html')