import pyodbc
from Util.dbutil import dbUtil

class DBConnection:
    # Constructor for establishing connection
    def __init__(self):
        conn_str = dbUtil.get_property_string()
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()
    # Method for closing connection
    def close(self):
        self.cursor.close()
        self.conn.close()