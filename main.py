import sqlite3
import os.path


def dbConnect():
    db = sqlite3.connect('config/database.db')
    print("Successfully Connected to database")
    return db


if os.path.exists('config/database.db'):
    print("Found database, connecting...")
    dbConnection = dbConnect()
    # print(dbConnection)
else:
    print("Database not found. Exiting")
    exit()


"""
[DEV INFO] QUERY EXAMPLE:

sqliteSelectQuery = "select sqlite_version();"
cursor.execute(sqliteSelectQuery)
record = cursor.fetchall()
print("SQLite Database Version is: ", record)
cursor.close()
"""
