import sqlite3

# cursor.execute(insert_command.format("Eugene", "Tsai"))
# cursor.execute(insert_command.format("Eudora", "Tsai"))
# cursor.execute(insert_command.format("Vincent", "Tsai"))
# cursor.execute(insert_command.format("Sumiaty", "Widjaja"))


def reinitialize_table(cursor, tablename):
    drop_command = "DROP TABLE {};"
    init_employee_command = """CREATE TABLE employee (
    fname VARCHAR(20),
    lname VARCHAR(20)
    );"""
    cursor.execute(drop_command.format(tablename))
    cursor.execute(init_employee_command)

def fetch_table(cursor, tablename):
    cursor.execute("""SELECT * FROM {};""".format(tablename))
    return cursor.fetchall()

def insert_to_table(cursor, tablename, content):
    insert_command = """INSERT INTO {} VALUES ("{}", "{}");"""
    cursor.execute(insert_command.format(tablename, content[0], content[1]))

def remove_from_table(cursor, tablename, content, attribute):
    remove_command = """DELETE FROM {} WHERE {}='{}';"""
    cursor.execute()