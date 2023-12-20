from util.DBConnUtil import dbConnection
def displayCourseInfo():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute("SELECT * FROM Course")
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR IN REtRIVAL {E}")
    finally:
        if conn:
            dbConnection.close(conn)
