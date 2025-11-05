from flask import Flask, jsonfy

app = Flask(__name__)

@app.router("/")
def index():
	return jsonify (("message": "it works! Student A00840297"))
if __name__ == "__main__":
	app.run(threaded=True, host='0.0.0.0', port=3000)
