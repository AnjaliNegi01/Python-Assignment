from util.DBConnUtil import dbConnection
def displayTeacherInfo():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT * FROM TEACHER ''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR DURING RETRIVAL")
    finally:
        if conn:
            dbConnection.close(conn)