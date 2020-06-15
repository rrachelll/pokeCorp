import pymysql

connection = pymysql.Connect(
    host="localhost",
    user="root",
    password="rachel123",
    db="PokeCorp",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
    )
if connection.open:
    print("the connection is opened")
