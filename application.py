from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route('/')
def hello():
    return render_template("index.html")

@application.route('/predict')
def predict():
    return "To be added very soon ;)"

if __name__ == "__main__":
	application.debug = True
	application.run()
