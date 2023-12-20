from util.DBConnUtil import dbConnection
from exception.studentNotFound import StudentNotFoundException
from exception.invalidStudentData import InvalidStudentDataException
def updateStudentInfo():
    StudentID=int(input("Enter Student ID: "))
    Email=input("Enter new Email ID: ")
    try:
        conn,stmt=dbConnection.open()
        # Check if the student is not found
        if not StudentNotFoundException.is_student_exists(StudentID, conn, stmt):
            raise StudentNotFoundException()
        
        if not InvalidStudentDataException.validate_email(Email):
            raise InvalidStudentDataException()

        data=[(Email,StudentID)]
        stmt.executemany('''UPDATE Student SET Email=%s WHERE StudentID=%s''',data)
        conn.commit()
        print("\nSTUDENT INFO UPDATED")
    except StudentNotFoundException as se:
        print(f"ERROR DURING ENROLLMENT: {se}")
    except InvalidStudentDataException as ise:
        print(f"Error during insertion: {ise}")
    except Exception as E:
        print(f"Error During Updation: {E}")
    finally:
        if conn:
            dbConnection.close(conn)