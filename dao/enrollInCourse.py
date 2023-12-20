from util.DBConnUtil import dbConnection
from exception.duplicateEnrollmentError import DuplicateEnrollmentException
from exception.studentNotFound import StudentNotFoundException
from exception.courseNotFound import CourseNotFoundException

def enrollInCourse():
    EnrollmentID = int(input("Enter Enrollment ID: "))
    StudentID = int(input("Enter Student ID: "))
    CourseID = int(input("Enter Course ID: "))
    EnrollmentDate = input("Enter Enrollment date: ")

    try:
        conn, stmt = dbConnection.open()

        # Check if the student is not found
        if not StudentNotFoundException.is_student_exists(StudentID, conn, stmt):
            raise StudentNotFoundException()

        # Check if the course is not found
        if not CourseNotFoundException.is_course_exists(CourseID, conn, stmt):
            raise CourseNotFoundException()

        # Check if the enrollment is a duplicate
        if DuplicateEnrollmentException.is_duplicate_enrollment(StudentID, CourseID, conn, stmt):
            raise DuplicateEnrollmentException()

        data = [(EnrollmentID, StudentID, CourseID, EnrollmentDate)]
        stmt.executemany('''INSERT INTO Enrollment(EnrollmentID, StudentID, CourseID, EnrollmentDate)
                            VALUES (%s, %s, %s, %s)''', data)
        conn.commit()
        print("STUDENT ENROLLED")

    except StudentNotFoundException as se:
        print(f"ERROR DURING ENROLLMENT: {se}")
    except CourseNotFoundException as ce:
        print(f"ERROR DURING ASSIGNING TEACHER: {ce}")
    except DuplicateEnrollmentException as de:
        print(f"ERROR DURING ENROLLMENT: {de}")
    except Exception as E:
        print(f"ERROR DURING ENROLLMENT: {E}")
    finally:
        if conn:
            dbConnection.close(conn)

