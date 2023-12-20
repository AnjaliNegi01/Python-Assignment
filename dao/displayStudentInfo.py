from util.DBConnUtil import dbConnection
def displayStudentInfo():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT * FROM Student''')
        record=stmt.fetchall()
        for i in record:
            print(i)
        return record
    except Exception as E:
        print(f"ERROR DURING DISPLAY {E}")
    finally:
        if conn:
            dbConnection.close(conn)
