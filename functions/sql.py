import sqlite3
from . import system


def database_connect():
    """
    Function to establish the database connection with SQLite3.
    """
    db = sqlite3.connect('database.db')
    print(system.infMsg + "Successfully connected to database")
    return db


def exec_query(db, query):
    """
    Function to execute query.
    It may disappear depending on project's evolution.
    """
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def insert_new_user(db, values):
    """
    Function to execute query.
    It may disappear depending on project's evolution.
    """
    sql = "INSERT INTO users(username, points) VALUES(?,?);"
    cursor = db.cursor()
    print(system.sysMsg + "Adding, user to database...")
    cursor.execute(sql, values)
    db.commit()
    print(system.infMsg + "User created correctly!")
    cursor.close()
