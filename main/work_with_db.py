import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="pp_lab6_website_user",
    database="pp_lab6_website_db",
    password="2509"
)

mycursor = mydb.cursor()

res = "DROP TABLE Someinfo;"
mycursor.execute(res)

res = "CREATE TABLE IF NOT EXISTS Someinfo (email varchar(30) PRIMARY KEY, phone_number varchar(13), name_ varchar(20), age smallint, has_auto bool);"
mycursor.execute(res)

query1 = "INSERT IGNORE INTO Someinfo(email, phone_number, name_, age, has_auto) VALUES ('MyEmail@gmail.com', '+38012345678', 'Michael','20','1');"
query2 = "INSERT IGNORE INTO Someinfo(email, phone_number, name_, age, has_auto) VALUES ('MyNewEmail@gmail.com', '+38077777777', 'Andrew','22','0');"
query3 = "INSERT IGNORE INTO Someinfo(email, phone_number, name_, age, has_auto) VALUES ('MyAnotherEmail@gmail.com', '+38048148533', 'John','19','0');"
mycursor.execute(query1)
mycursor.execute(query2)
mycursor.execute(query3)

res = "Select * from Someinfo;"
mycursor.execute(res)
rows = mycursor.fetchall()
for row in rows:
    print(row)

mydb.commit()
mydb.close()
