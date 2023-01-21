from config import SQL_DRIVER, SQL_SERVER, SQL_DB, SQL_USER, SQL_PWD
import pyodbc

def conn_string(driver, server, db, user, pwd):
    """
    Create and return sql server connection string
    """
    return f"Driver={driver};Server={server};Database={db};Authentication=SqlPassword;Encrypt=yes;TrustServerCertificate=Yes;UID={user};PWD={pwd}"

# create database connection instance
def conn_odbc(driver=SQL_DRIVER, server=SQL_SERVER, db=SQL_DB, user=SQL_USER, pwd=SQL_PWD):
    """
    Create and return database connection instance
    """
    try:
        conn = pyodbc.connect(conn_string(driver, server, db, user, pwd))
        return conn
    except pyodbc.Error as e:
        print("Connection Error:")
        print(e.args[1])

# execute sql statement
def select_records(cnxn, query):
    """
    Create cursor connection, execute sql query, and return all fetched records
    """
    try:
        cursor = cnxn.cursor()
        cursor.execute(query)
        if cursor.rowcount != -1:
            rows = cursor.fetchall()
            cursor.commit()
            return rows
        else:
            cursor.commit()
    except Exception as e:
        cursor.rollback()
        print(e.args[1])
    finally:
        cursor.close()
        cnxn.close()

def update_records(cnxn, query):
    """
    Create cursor connection, execute sql update query
    """
    try:
        cursor = cnxn.cursor()
        cursor.execute(query)
        cursor.commit()
    except Exception as e:
        cursor.rollback()
        print(e.args[1])
    finally:
        cursor.close()
        cnxn.close()

# execute sql insert statement
def insert_records(cnxn, query, params):
    """
    Create cursor connection, execute sql query, and return all fetched records
    """
    try:
        cursor = cnxn.cursor()
        cursor.executemany(query, params)
        if cursor.rowcount != -1:
            rows = cursor.fetchall()
            cursor.commit()
            return rows
        else:
            cursor.commit()
    except Exception as e:
        cursor.rollback()
        print(e.args[1])
    finally:
        cursor.close()
        cnxn.close()

# function to read file contents
def read_contents(path):
    with open(path, "r") as file:
        contents = file.read()
    return contents