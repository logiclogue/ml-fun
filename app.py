from flask import Flask,url_for,render_template,request,redirect

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
	return render_template("index.html")

@app.route("/result",methods=["POST"])
def result():
	print(request.get_json())
	return "works!"

if __name__ == '__main__':
	app.run(debug=True)
