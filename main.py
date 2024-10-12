# importing sqlite3
import sqlite3
#importing pandas
import pandas as pd
# Establish a connection to the SQLite database
connection = sqlite3.connect("database.sqlite")
print("Lucky you, the connection is established and at the end get out here!!!!!!!!!!!!!!!")
# Reading data from the Match table
tables = pd.read_sql("SELECT * FROM Match", connection)
print(tables)
# Calculating the average win margin
tables = pd.read_sql("SELECT AVG(Win_Margin) FROM Match", connection)
print(tables.info())


