from util.DBConnUtil import dbConnection
def addStudents():
    StudentID=int(input("Enter Student ID: "))
    FirstName=input("Enter First Name: ")
    LastName=input("Enter Last Name: ")
    DateOfBirth=input("Enter Date of Birth: ")
    Email=input("Enter Email ID: ")
    PhoneNumber=input("Enter Phone Number: ")

    try:
        conn,stmt=dbConnection.open()

        data=[(StudentID,FirstName,LastName,DateOfBirth,Email,PhoneNumber)]
        stmt.executemany('''INSERT INTO Student(StudentID,FirstName,LastName,DateOfBirth,Email,PhoneNumber)
                            VALUES(%s,%s,%s,%s,%s,%s)''',data)
        conn.commit()
        print("NEW STUDENT ADDED")
    except Exception as E:
        print(f"Error during insertion: {E}")
    finally:
        if conn:
            dbConnection.close(conn)