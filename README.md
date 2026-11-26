# CyberSec-Project
OVERVIEW:
This is a python application that can be connected to an Oracle and PostGreSQL database to run queries that test different injection methods. 



SET UP:
Download and Install PostGreSQL: https://www.postgresql.org/download/ 
Download and Install OracleDBAI: https://www.oracle.com/ 
The OracleDBAI involves setting up an account on oracle.

Download and install python and the following python libraries: flask, oracledb and psycopg2
In the app.py file replace Oracle and PostGreSQL connections with those that match your databases. 
Run the Python file. 
Open a Broswer and search http://127.0.0.1:5000/ to open your local session. 

Maximilian Krishka-Pachal - 200536378 incorporated the flask and setup the html pages
Hunter Ruel - 200403482 Setup database connections and ran injection tests. Also added the python libraries oracldb and psycopg2

The SQL folder contains the queries to run in your PostgreSQL and OracleDB to setup a North Wind example.
The Template folder contains the HTML that the viewer sees. The static folder contains the CSS for the styling of the local application.
The app.py is the file that runs the application and manages most of the logic.
