from util.DBConnUtil import dbConnection
from exception.courseNotFound import CourseNotFoundException
def getEnrollment():
    CourseID=int(input("\nEnter Course ID: "))
    try:
        conn,stmt=dbConnection.open()
        if not CourseNotFoundException.is_course_exists(CourseID, conn, stmt):
            raise CourseNotFoundException()

        data=[(CourseID)]
        stmt.execute('''SELECT S.StudentID,S.FirstName,S.LastName,C.CourseName from Student AS S
                        JOIN Enrollment as E ON E.StudentID=S.StudentID
                        JOIN Course as C on C.CourseID=E.CourseID
                        WHERE CourseName=%s''',data)
        record=stmt.fetchall()
        for i in record:
            print(i)
    
    except CourseNotFoundException as ce:
        print(f"ERROR DURING ASSIGNING TEACHER: {ce}")
    except Exception as E:
        print(f"ERROR DURING RETRIVAL")
    finally:
        if conn:
            dbConnection.close(conn)
