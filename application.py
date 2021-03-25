from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route('/')
def index():
    return render_template("index.html")

@application.route('/improve-eth-ux')
def improve_eth_ux():
    return render_template("improve-eth-ux.html")

if __name__ == "__main__":
	application.debug = True
	application.run()
