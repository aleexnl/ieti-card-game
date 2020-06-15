import sqlite3
from . import system


def database_connect():
    """Function to establish the database connection."""
    database = sqlite3.connect('database.db')
    print(system.infMsg + "Successfully connected to database")
    return database


def exec_query(database, query):
    """Function to execute query. It may disappear depending on project's evolution."""
    cursor = database.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def insert_new_user(database, values):
    """Function to insert new users."""
    sql = "INSERT INTO users(username, points) VALUES(?,?);"
    cursor = database.cursor()
    print(system.sysMsg + "Adding, user to database...")
    cursor.execute(sql, values)
    database.commit()
    print(system.infMsg + "User created correctly!")
    cursor.close()
