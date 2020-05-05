import sqlite3
from schedulersql import *

def restore_db(cursor):
    return reinitialize_table(cursor, "employee")

def add_employee(cursor, content):
    return insert_to_table(cursor, "employee", content)

def remove_employee(cursor, content, attribute):
    return remove_from_table(cursor, "employee", content, attribute)

def retrieve_employees(cursor):
    return fetch_table(cursor, "employee")

def create_new_schedule(cursor):
    pass

def print_last_schedule(cursor):
    pass

def job_create_new_schedule(cursor):
    pass


def job_print_last_schedule(cursor):
    pass


def job_retrieve_employees(cursor):
    return retrieve_employees(cursor)


def job_add_employee(cursor):
    fname = input("Employee First Name: ")
    lname = input("Employee Last Name: ")
    return add_employee(cursor, [fname, lname])


def job_remove_employee(cursor):
    fname = input("Employee First Name: ")
    lname = input("Employee Last Name: ")
    return remove_employee(cursor, [fname, lname], ["fname", "lname"])


def job_restore_db(cursor):
    return restore_db(cursor)


def job_quit(cursor):
    print("Saving data and quitting program...")
    return 2


def invalid_cmd(cursor):
    print("Invalid Command")
    return 0


def prompt_command(cursor):
    print("Welcome to scheduler:")
    print("The following commands are available:")
    print("1. Create New Schedule")
    print("2. See Last Created Schedule")
    print("3. See List Of Employee")
    print("4. Add Employee")
    print("5. Remove Employee")
    print("6. Clear Employees")
    print("7, To Quit Program")
    cmd = int(input(": "))
    cmd_switcher = {
        1: job_create_new_schedule,
        2: job_print_last_schedule,
        3: job_retrieve_employees,
        4: job_add_employee,
        5: job_remove_employee,
        6: job_restore_db,
        7: job_quit
    }
    func = cmd_switcher.get(cmd, lambda: invalid_cmd)
    ret = func(cursor)
    if ret == 1:
        print("Command failed")
    return ret


if __name__ == "__main__":
    connection = sqlite3.connect("table.db")
    cursor = connection.cursor()
    return_status = 0
    while return_status != 2:
        return_status = prompt_command(cursor)

    connection.commit()
    connection.close()


# TODO
# * Change first name last name system to name string system
# Add a search by attribute functionality
# Add a create table by given attribute functionality (REACH)
# Figure how to randomly assign slots
# * Add a employee serial number
# * Change delete by selected attribute