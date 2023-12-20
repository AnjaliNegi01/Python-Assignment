import mysql.connector as sql
from util.DBPropertyUtil import DBPropertyUtil

class dbConnection:
    def open():
        try:
            s=DBPropertyUtil.get_property_string()
            conn=sql.connect(host=s[0],username=s[1],database=s[2],password=s[3])
            stmt=conn.cursor()
            return conn,stmt
        except Exception as E:
            print(E)
            return None,None
    def close(conn):
        try:
            conn.close()
            print("CONNECTION CLOSED")
        except Exception as E:
            print(E)
