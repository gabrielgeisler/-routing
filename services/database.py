import pyodbc

server = 'DESKTOP-10R6BMU\SQLEXPRESS' 
database = 'routing' 
username = 'sa' 
password = '123' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()