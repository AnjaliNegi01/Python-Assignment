from util.DBConnUtil import dbConnection
from exception.teacherNotFound import TeacherNotFoundException
from exception.invalidTeacherData import InvalidTeacherDataException
def updateTeacherInfo():
    TeacherID=int(input("Enter Teacher ID: "))
    Email=input("Enter new Email ID: ")
    try:
        conn,stmt=dbConnection.open()
        # Check if the teacher is not found
        if not TeacherNotFoundException.is_teacher_exists(TeacherID, conn, stmt):
            raise TeacherNotFoundException()

        if not InvalidTeacherDataException.validate_email(Email):
            raise InvalidTeacherDataException()
        data=[(Email,TeacherID)]
        stmt.executemany('''UPDATE Teacher SET Email=%s WHERE TeacherID=%s''',data)
        conn.commit()
        print("\nTeacher INFO UPDATED")
    except TeacherNotFoundException as te:
        print(f"ERROR DURING UPDATION: {te}")
    except InvalidTeacherDataException as ise:
        print(f"Error during insertion: {ise}")
    except Exception as E:
        print(f"Error During Updation: {E}")
    finally:
        if conn:
            dbConnection.close(conn)