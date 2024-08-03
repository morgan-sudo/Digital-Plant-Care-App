import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(conn, user):
    """ create a new user """
    sql = ''' INSERT INTO users(username, email, password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def create_plant(conn, plant):
    """ create a new plant """
    sql = ''' INSERT INTO plants(name, watering_schedule, light_requirements, user_id)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, plant)
    conn.commit()
    return cur.lastrowid

def create_care_task(conn, task):
    """ create a new care task """
    sql = ''' INSERT INTO care_tasks(plant_id, task_name, task_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def create_growth_note(conn, note):
    """ create a new growth note """
    sql = ''' INSERT INTO growth_notes(plant_id, note_date, description)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, note)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"db/plants.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        username TEXT NOT NULL,
                                        email TEXT NOT NULL UNIQUE,
                                        password TEXT NOT NULL
                                    ); """

    sql_create_plants_table = """ CREATE TABLE IF NOT EXISTS plants (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        watering_schedule TEXT NOT NULL,
                                        light_requirements TEXT NOT NULL,
                                        user_id INTEGER NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id)
                                    ); """

    sql_create_care_tasks_table = """ CREATE TABLE IF NOT EXISTS care_tasks (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        plant_id INTEGER NOT NULL,
                                        task_name TEXT NOT NULL,
                                        task_date DATE NOT NULL,
                                        FOREIGN KEY (plant_id) REFERENCES plants (id)
                                    ); """

    sql_create_growth_notes_table = """ CREATE TABLE IF NOT EXISTS growth_notes (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        plant_id INTEGER NOT NULL,
                                        note_date DATE NOT NULL,
                                        description TEXT NOT NULL,
                                        FOREIGN KEY (plant_id) REFERENCES plants (id)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_plants_table)
        create_table(conn, sql_create_care_tasks_table)
        create_table(conn, sql_create_growth_notes_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
