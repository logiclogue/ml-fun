from flask import Flask,url_for,render_template,request,redirect
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	return render_template("index.html")

@app.route("/result",methods=["POST"])
def result():
    data = np.array(request.get_json())
    weights = joblib.load('weights.pkl')

    val = np.argmax(np.dot(data, weights))

    return str(val)

if __name__ == '__main__':
	app.run(debug=True)
