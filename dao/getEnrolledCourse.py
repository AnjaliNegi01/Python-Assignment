from util.DBConnUtil import dbConnection
def getEnrolledCourse():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT Course.CourseID,CourseName from Course
                        JOIN Enrollment ON Enrollment.EnrollmentID=Course.CourseID''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR DURING RETRIVAL {E}")
    finally:
        if conn:
            dbConnection.close(conn)