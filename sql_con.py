import pyodbc

class SQLConnection:
    def __init__(self, driver, server, db, user, pwd):
        self.driver = driver
        self.server = server
        self.db = db
        self.user = user
        self.pwd = pwd

    def get_conn_string(self):
        return f"Driver={self.driver};Server={self.server};Database={self.db};Authentication=SqlPassword;Encrypt=yes;TrustServerCertificate=Yes;UID={self.user};PWD={self.pwd}"
    
    def get_conn_odbc(self):
        try:
            conn = pyodbc.connect(self.get_conn_string())
            return conn
        except pyodbc.Error as e:
            print("Connection Error:")
            print(e.args[1])

    def select_records(self, query):
        cnxn = self.get_conn_odbc()
        try:
            cursor = cnxn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cnxn.commit()
            return rows
        except Exception as e:
            cnxn.rollback()
            print(e.args[1])
        finally:
            cursor.close()
            cnxn.close()

    def insert_records(self, query, params):
        cnxn = self.get_conn_odbc()
        try:
            cursor = cnxn.cursor()
            cursor.executemany(query, params)
            cnxn.commit()
        except Exception as e:
            cnxn.rollback()
            print(e.args[1])
        finally:
            cursor.close()
            cnxn.close()

    def execute_ddl_dml(self, query):
        cnxn = self.get_conn_odbc()
        try:
            cursor = cnxn.cursor()
            cursor.execute(query)
            cnxn.commit()
        except Exception as e:
            cnxn.rollback()
            print(e.args[1])
        finally:
            cursor.close()
            cnxn.close()


# function to read file contents
def read_contents(path):
    with open(path, "r") as file:
        contents = file.read()
    return contents



# Summary of how to use this module

# from config import SQL_DRIVER, SQL_SERVER, SQL_DB, SQL_USER, SQL_PWD
# print("Hello World!")
# a = SQLConnection(SQL_DRIVER, SQL_SERVER, SQL_DB, SQL_USER, SQL_PWD)
# # rows = a.select_records("select top 3 * from bank_stocks")
# # print(rows)

# query = """
# update bank_stocks
# set Ticker = 'BAC' 
# where Ticker = 'SVB'
# """
# a.execute_ddl_dml(query)

# query = """
# insert into bank_stocks
# values (?, ?, ?, ?, ?, ?, ?, ?, getdate())
# """
# a.insert_records(query, [('2023-01-01', 'SVB', 1, 1, 1, 1, 1, 1),
# ('2022-01-02', 'SVB', 1, 1, 1, 1, 1, 1),
# ('2022-01-03', 'SVB', 1, 1, 1, 1, 1, 1),
# ('2022-01-04', 'SVB', 1, 1, 1, 1, 1, 1),
# ('2022-01-05', 'SVB', 1, 1, 1, 1, 1, 1)])

# query = """
# if object_id('bank_stocks') is not null
# 	drop table bank_stocks;
# create table bank_stocks (
# Date date not null,
# Ticker varchar(10) not null,
# Adj_Close numeric(9, 6) not null,
# Close_Price numeric(9, 6) not null,
# High_Price numeric(9, 6) not null,
# Low_Price numeric(9, 6) not null,
# Open_Price numeric(9, 6) not null,
# Volume int not null,
# Created datetime not null
# primary key (Date, Ticker)
# );
# """
