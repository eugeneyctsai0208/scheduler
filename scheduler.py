import sqlite3
from schedulersql import *

def restore_db_memory(cursor):
    reinitialize_table(cursor, "employee")

def add_employee(cursor, fname, lname):
    insert_to_table(cursor, "employee", [fname, lname])

def remove_employee(cursor, fname, attribute):
    remove_from_table(cursor, "employee", fname, attribute)

def retrieve_employees(cursor):
    return fetch_table(cursor, "employee")

def prompt_command():
    print("Welcome to scheduler:")
    print("The following commands are available:")
    print("1. Create New Schedule")
    print("2. See Last Created Schedule")
    print("3. See List Of Employee")
    print("4. Add Employee")
    print("5. Remove Employee")

if __name__ == "__main__":
    connection = sqlite3.connect("table.db")
    cursor = connection.cursor()

    while True:
        return_status = prompt_command()

    connection.commit()
    connection.close()