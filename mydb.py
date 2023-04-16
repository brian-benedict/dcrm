import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd= 'Adelimarsi1!',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("all done!")