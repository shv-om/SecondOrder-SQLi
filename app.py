from flask import Flask, request, render_template, redirect, Response
import requests

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/create_query', methods=["GET"])
def create_query():

	# Returns the Result if Proxy servers check is completed and validated.
	# This is the dummy data that we are sending to make sure our proxy and main server can communicate.

	return "The values are not SQL injection payloads"


if __name__ == '__main__':
	app.run(debug=True, port=9000)