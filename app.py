"""

Project for testing DBMSs against SQL Injections and also their protections and defences

This application displays different pages for different injection types and returns query results
from several different databases to demonstrate how DBMSs react differently to SQLi attempts.
Also to show different protection methods and how they hold up in different DBMSs.

Max Krishka-Pachal 200526378

"""


from flask import Flask, render_template, url_for, redirect, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for("union"))



@app.route('/union', methods=["GET", "POST"])
def union():
	query = ""
	chosen_tab = "none"
	dbms_name = random.randint(1, 100);
	dbms_result = random.randint(1, 100);

	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		dbms_name = random.randint(1, 100);
		dbms_result = random.randint(1, 100);

	return render_template('union.html', query=query, chosen_tab=chosen_tab, dbms_name=dbms_name, dbms_result=dbms_result)


@app.route('/error', methods=["GET", "POST"])
def error():
	query = request.args.get("q", "")
	tab = request.args.get("tab", "none")
	return render_template('error.html', dbms_name="test", dbms_result="test")


@app.route('/blindbool', methods=["GET", "POST"])
def blind_bool():
	return render_template('blind_bool.html', dbms_name="test", dbms_result="test")


@app.route('/blindtime', methods=["GET", "POST"])
def blind_time():
	return render_template('blind_time.html', dbms_name="test", dbms_result="test")


@app.route('/secondorder', methods=["GET", "POST"])
def second_order():
	return render_template('second_order.html', dbms_name="test", dbms_result="test")


@app.route('/stackedquery', methods=["GET", "POST"])
def stacked_query():
	return render_template('stacked_query.html', dbms_name="test", dbms_result="test")


@app.errorhandler(404)
def not_found(error):
	return redirect(url_for("union"))


if __name__ == '__main__':
	app.run(debug=True)