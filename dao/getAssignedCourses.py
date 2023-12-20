from util.DBConnUtil import dbConnection
def getAssignedCourses():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT C.CourseName,T.FirstName,T.LastName FROM Course as C
                        JOIN Teacher as T on T.TeacherID=C.TeacherID''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR DURING RETRIVAL")
    finally:
        if conn:
            dbConnection.close(conn)
