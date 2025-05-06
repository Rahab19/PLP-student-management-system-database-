import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mypassword",
    database="student_portal"
)

cursor = connection.cursor(dictionary=True)
