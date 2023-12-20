from util.DBConnUtil import dbConnection
def getStudent():
    EnrollmentID=int(input("\nEnter Enrollment ID:"))
    try:
        conn,stmt=dbConnection.open()
        data=[(EnrollmentID)]
        stmt.execute('''SELECT S.StudentID,S.FirstName,S.LastName FROM Student AS S
                        JOIN Enrollment AS E ON E.StudentID=S.StudentID
                        WHERE E.EnrollmentID=%s''',data)
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR DURING RETRIVAL {E}")
    finally:
        if conn:
            dbConnection.close(conn)