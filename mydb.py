import mysql.connector

dateBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Pandu719822$"
)

cursorObject =dateBase.cursor()

cursorObject.execute("create database naik")

print("Database created")