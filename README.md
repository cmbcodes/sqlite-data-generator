Vehicle Database - README
This repository contains scripts to generate a mock vehicle database using Python and SQLite. The database consists of tables for vehicles, manufacturers, owners, and maintenance records.

Instructions
Python Script to Generate Database
Modify Loop Counts:

Open the generate_vehicle_data.py file.
Edit the loop ranges to adjust the number of records to be generated for each table.
Modify loop counts in the sections marked with comments (e.g., for _ in range(10):, for _ in range(20):, etc.) according to your desired number of records.

Run Python Script:
Run the Python script generate_vehicle_data.py to populate the SQLite database.
In bash:
python generate_vehicle_data.py

Executing the SQL Test Script

Running the Test Script:
Open a SQLite database management tool or use the command line.
Make sure you have the SQLite database file vehicles.db generated by the Python script.

Execute the SQL Script:
Open the query_script.sql file.
Run the SQL queries from query_script.sql against the vehicles.db database using your SQLite tool or command line:
In bash:
sqlite3 vehicles.db < query_script.sql

Review Results:
Check the output of the executed SQL queries to verify data retrieval and test different SELECT statements against the populated database.
