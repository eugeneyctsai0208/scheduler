import sqlite3

def reinitialize_table(cursor, tablename):
    drop_command = "DROP TABLE {};"
    init_employee_command = """CREATE TABLE employee (
    fname VARCHAR(20),
    lname VARCHAR(20)
    );"""
    try:
        cursor.execute(drop_command.format(tablename))
        print("Dropped database {}".format(tablename))
    except:
        print("Existing database not found! Proceed to creating...")
        pass
    try:
        cursor.execute(init_employee_command)
        print("Created TABLE employee: (first_name, last_name)")
    except:
        return 1
    return 0

def fetch_table(cursor, tablename):
    try:
        cursor.execute("""SELECT * FROM {};""".format(tablename))
    except:
        return 1
    print(cursor.fetchall())
    return 0

def insert_to_table(cursor, tablename, content):
    insert_command = """INSERT INTO {} VALUES ("{}", "{}");"""
    try:
        cursor.execute(insert_command.format(tablename, content[0], content[1]))
    except:
        return 1
    return 0

def remove_from_table(cursor, tablename, content, attribute):
    remove_command = """DELETE FROM {} WHERE {}='{}' AND {}='{}';"""
    try:
        cursor.execute(remove_command.format(tablename, attribute[0], content[0], attribute[1], content[1]))
    except:
        return 1
    return 0