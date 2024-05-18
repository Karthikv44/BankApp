import pyodbc
from Util.dbutil import dbUtil

class DBConnection:
    def __init__(self):
        conn_str = dbUtil.get_property_string()
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()