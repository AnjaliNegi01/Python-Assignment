from util.DBConnUtil import dbConnection
from exception.courseNotFound import CourseNotFoundException
def getTeacher():
    CourseID=input("Enter Course ID: ")
    try:
        conn,stmt=dbConnection.open()
        if not CourseNotFoundException.is_course_exists(CourseID, conn, stmt):
            raise CourseNotFoundException()
        data=[(CourseID)]
        stmt.execute('''SELECT T.TeacherId,T.FirstName,T.LastName,C.CourseName FROM Course as C
                        JOIN Teacher AS T ON T.TeacherID=C.TeacherID
                        WHERE C.CourseName=%s''',data)
        record=stmt.fetchall()
        for i in record:
            print(i)
    
    except CourseNotFoundException as ce:
        print(f"ERROR DURING ASSIGNING TEACHER: {ce}")
    except Exception as E:
        print(f"ERROR DURING RETRIVAL {E}")
    finally:
        if conn:
            dbConnection.close(conn)
    