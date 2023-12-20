from util.DBConnUtil import dbConnection
from exception.teacherNotFound import TeacherNotFoundException
def assignTeacher():
    CourseID=int(input("Enter Course ID: "))
    CourseName=input("Enter Course Name: ")
    Credit=int(input("Enter Credit: "))
    TeacherID=int(input("Enter Teacher ID: "))
    try:
        conn,stmt=dbConnection.open()
        if not TeacherNotFoundException.is_teacher_exists(TeacherID, conn, stmt):
            raise TeacherNotFoundException()

        data=[(CourseID,CourseName,Credit,TeacherID)]
        stmt.executemany('''INSERT INTO Course (CourseID,CourseName,Credit,TeacherId)
                            VALUES(%s,%s,%s,%s)''',data)
        conn.commit()
        print("TEACHER ASSIGNED")
    
    except TeacherNotFoundException as te:
        print(f"ERROR: {te}")
    except Exception as E:
        print(f"ERROR DURING ASSIGNING TEACHER")
    finally:
        if conn:
            dbConnection.close(conn)
