"""

Project for testing DBMSs against SQL Injections and also their protections and defences

This application displays different pages for different injection types and returns query results
from several different databases to demonstrate how DBMSs react differently to SQLi attempts.
Also to show different protection methods and how they hold up in different DBMSs.

Max Krishka-Pachal 200526378

"""


from flask import Flask, render_template, url_for, redirect, jsonify, request
import random
import oracledb
import psycopg2
#Establishing connection to local oracle database
oracleConnection = oracledb.connect(
	user="SYSTEM",
	password = "EasyPassword1!",
	dsn = "localhost/FREE"
)
#Variable to run oracle queries
oracleCursor = oracleConnection.cursor()
#oracleCursor.execute("SELECT * FROM customers;")
#print("This is the oracle connection test: ", oracleCursor.fetchall())
#Postgress DB connection 
postgressConnection = psycopg2.connect(
	database='postgres', 
	user="postgres", 
	password ="EasyPassword1!", 
	host='localhost', 
	port=5432
	)
pythonCursor = postgressConnection.cursor()
#pythonCursor.execute("SELECT * FROM customers;")
#print("This is the PostGress connection test: ", pythonCursor.fetchall())



app = Flask(__name__)

@app.route('/')
def index():
	return redirect(url_for("union"))



@app.route('/union', methods=["GET", "POST"])
def union():
	query = ""
	queryExc=""
	chosen_tab = "none"
	dbms_name = "PostgreSQL result";
	dbms_result = "OracleDB result";
	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		queryExc="SELECT * FROM CUSTOMERS where customer_id = " +"\'" +query + "\'"
		print("THIS IS THE CHOSEN TAB" + chosen_tab)
		if chosen_tab == "none":
			try:
				#execute PostgreSQL
				pythonCursor.execute(queryExc)
				dbms_name = pythonCursor.fetchall()

			except psycopg2.Error as e:
				print(e.pgerror)
				dbms_name = e.pgerror
				postgressConnection.rollback()

			try:
				#execute OracleSQL
				oracleCursor.execute(queryExc)
				dbms_result = oracleCursor.fetchall()
			except oracledb.Error as error:
				print(error.args)	
				dbms_result = error.args
		if chosen_tab == 'protection 1':
			print("Modify queries here HELLO DUDE")

		if chosen_tab == 'protection 2':
			print("Run protection2: HELLO TO YOU TWO")

		
		

	return render_template('union.html', query=query, chosen_tab=chosen_tab, dbms_name=dbms_name, dbms_result=dbms_result)


@app.route('/error', methods=["GET", "POST"])
def error():
	query = ""
	queryExc=""
	chosen_tab = "none"
	dbms_name = "PostgreSQL result";
	dbms_result = "OracleDB result";
	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		queryExc="SELECT * FROM CUSTOMERS where customer_id = " +"\'" +query + "\'"
		print("THIS IS THE CHOSEN TAB" + chosen_tab)
		if chosen_tab == "none":
			try:
				#execute PostgreSQL
				pythonCursor.execute(queryExc)
				dbms_name = pythonCursor.fetchall()

			except psycopg2.Error as e:
				print(e.pgerror)
				dbms_name = e.pgerror
				postgressConnection.rollback()

			try:
				#execute OracleSQL
				oracleCursor.execute(queryExc)
				dbms_result = oracleCursor.fetchall()
			except oracledb.Error as error:
				print(error.args)	
				dbms_result = error.args
		if chosen_tab == 'protection 1':
			print("Modify queries here HELLO DUDE")

		if chosen_tab == 'protection 2':
			print("Run protection2: HELLO TO YOU TWO")
	return render_template('error.html', dbms_name="test", dbms_result="test")


@app.route('/blindbool', methods=["GET", "POST"])
def blind_bool():
	query = ""
	queryExc=""
	chosen_tab = "none"
	dbms_name = "PostgreSQL result";
	dbms_result = "OracleDB result";
	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		queryExc="SELECT * FROM CUSTOMERS where customer_id = " +"\'" +query + "\'"
		print("THIS IS THE CHOSEN TAB" + chosen_tab)
		if chosen_tab == "none":
			try:
				#execute PostgreSQL
				pythonCursor.execute(queryExc)
				dbms_name = pythonCursor.fetchall()

			except psycopg2.Error as e:
				print(e.pgerror)
				dbms_name = e.pgerror
				postgressConnection.rollback()

			try:
				#execute OracleSQL
				oracleCursor.execute(queryExc)
				dbms_result = oracleCursor.fetchall()
			except oracledb.Error as error:
				print(error.args)	
				dbms_result = error.args
		if chosen_tab == 'protection 1':
			print("Modify queries here HELLO DUDE")

		if chosen_tab == 'protection 2':
			print("Run protection2: HELLO TO YOU TWO")
	return render_template('blind_bool.html', dbms_name="test", dbms_result="test")


@app.route('/blindtime', methods=["GET", "POST"])
def blind_time():
	query = ""
	queryExc=""
	chosen_tab = "none"
	dbms_name = "PostgreSQL result";
	dbms_result = "OracleDB result";
	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		queryExc="SELECT * FROM CUSTOMERS where customer_id = " +"\'" +query + "\'"
		print("THIS IS THE CHOSEN TAB" + chosen_tab)
		if chosen_tab == "none":
			try:
				#execute PostgreSQL
				pythonCursor.execute(queryExc)
				dbms_name = pythonCursor.fetchall()

			except psycopg2.Error as e:
				print(e.pgerror)
				dbms_name = e.pgerror
				postgressConnection.rollback()

			try:
				#execute OracleSQL
				oracleCursor.execute(queryExc)
				dbms_result = oracleCursor.fetchall()
			except oracledb.Error as error:
				print(error.args)	
				dbms_result = error.args
		if chosen_tab == 'protection 1':
			print("Modify queries here HELLO DUDE")

		if chosen_tab == 'protection 2':
			print("Run protection2: HELLO TO YOU TWO")
	return render_template('blind_time.html', dbms_name="test", dbms_result="test")


@app.route('/secondorder', methods=["GET", "POST"])
def second_order():
	query = ""
	queryExc=""
	chosen_tab = "none"
	dbms_name = "PostgreSQL result";
	dbms_result = "OracleDB result";
	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		queryExc="SELECT * FROM CUSTOMERS where customer_id = " +"\'" +query + "\'"
		print("THIS IS THE CHOSEN TAB" + chosen_tab)
		if chosen_tab == "none":
			try:
				#execute PostgreSQL
				pythonCursor.execute(queryExc)
				dbms_name = pythonCursor.fetchall()

			except psycopg2.Error as e:
				print(e.pgerror)
				dbms_name = e.pgerror
				postgressConnection.rollback()

			try:
				#execute OracleSQL
				oracleCursor.execute(queryExc)
				dbms_result = oracleCursor.fetchall()
			except oracledb.Error as error:
				print(error.args)	
				dbms_result = error.args
		if chosen_tab == 'protection 1':
			print("Modify queries here HELLO DUDE")

		if chosen_tab == 'protection 2':
			print("Run protection2: HELLO TO YOU TWO")
	return render_template('second_order.html', dbms_name="test", dbms_result="test")


@app.route('/stackedquery', methods=["GET", "POST"])
def stacked_query():
	query = ""
	queryExc=""
	chosen_tab = "none"
	dbms_name = "PostgreSQL result";
	dbms_result = "OracleDB result";
	if request.method == "POST":
		query = request.form.get("query", "")
		chosen_tab = request.form.get("tab_choice") or request.form.get("chosen_tab", "none")
		queryExc="SELECT * FROM CUSTOMERS where customer_id = " +"\'" +query + "\'"
		print("THIS IS THE CHOSEN TAB" + chosen_tab)
		if chosen_tab == "none":
			try:
				#execute PostgreSQL
				pythonCursor.execute(queryExc)
				dbms_name = pythonCursor.fetchall()

			except psycopg2.Error as e:
				print(e.pgerror)
				dbms_name = e.pgerror
				postgressConnection.rollback()

			try:
				#execute OracleSQL
				oracleCursor.execute(queryExc)
				dbms_result = oracleCursor.fetchall()
			except oracledb.Error as error:
				print(error.args)	
				dbms_result = error.args
		if chosen_tab == 'protection 1':
			print("Modify queries here HELLO DUDE")

		if chosen_tab == 'protection 2':
			print("Run protection2: HELLO TO YOU TWO")
	return render_template('stacked_query.html', dbms_name="test", dbms_result="test")


@app.errorhandler(404)
def not_found(error):
	return redirect(url_for("union"))


if __name__ == '__main__':
	app.run(debug=True)