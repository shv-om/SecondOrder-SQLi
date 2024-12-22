from flask import Flask, request, redirect, Response
import requests
import random

app = Flask(__name__)
SITE_NAME = 'http://localhost:9000/'

sql_statements = ('SELECT', 'UPDATE', 'WHERE', 'UNION', 'SET', 'JOIN', 'HAVE', 'FROM', 'ORDER', 'GROUP', 'INSERT', 'DELETE', 'CREATE', 'ALTER', 'DROP')

def add_random(original_query):
	# Add the magic number at the end of every SQL keyword in the given query.
	# Returns the updated query and the magin number.

	global sql_statements

	num_key = str(random.choice(range(100, 999)))

	for word in original_query.split(' '):
		if word in sql_statements:
			original_query = original_query.replace(word, word+num_key)

	return original_query, num_key


def check_query(query, num_key):
	# Checks the given query if all the SQL keywords contains the magic number at the end or not.
	# Returns a flag value to determine if the query pass the test or it's a second order SQL injection attempt.

	global sql_statements

	flag = False

	for word in query.split(' '):
		if word in sql_statements:
			if not word.endswith(num_key):
				flag = True
				return flag

	return flag


@app.route('/<path:path>')
def create_query(path):
	global SITE_NAME

	resp = requests.get(f"{SITE_NAME}{path}")
	excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
	headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]

	original_query = "UPDATE Users SET username= {} , password= {} , email= {} WHERE usemame={}"

	original_query, num_key = add_random(original_query.upper())

	username = request.args['username']
	password = request.args['password']
	email = request.args['email']

	query = original_query.format(username, password, email, username)
	print(query)

	flag = check_query(query.upper(), num_key)

	if flag:
		response = "Warning! Second Order SQL Injection Detected."
	else:
		response = Response(resp.content, resp.status_code, headers)
		# response = Response(query, resp.status_code, headers)

	return response


@app.route("/", defaults={'path': ''})
# @app.route("/<path:path>", methods=["GET","POST"])
def proxy(path):
	global SITE_NAME
	if request.method=="GET":
		resp = requests.get(f"{SITE_NAME}{path}")
		excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
		headers = [(name, value) for (name, value) in  resp.raw.headers.items() if name.lower() not in excluded_headers]
		response = Response(resp.content, resp.status_code, headers)
		
		return response

	elif request.method=="POST":
		resp = requests.post(f"{SITE_NAME}{path}", data=request.form)
		excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
		headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
		response = Response(resp.content, resp.status_code, headers)

		return response


if __name__ == '__main__':
	app.run(debug=True, port=8081)
