from util.DBConnUtil import dbConnection

def addTeacher():
    TeacherID=int(input("Enter Teacher ID: "))
    FirstName=input("Enter First Name: ")
    LastName=input("Enter Last Name: ")
    Email=input("Enter Email: ")
    try:
        conn,stmt=dbConnection.open()
        data=[(TeacherID,FirstName,LastName,Email)]
        stmt.executemany('''INSERT INTO Teacher(TeacherID,FirstName,LastName,Email)
                            VALUES(%s,%s,%s,%s)''',data)
        conn.commit()
        print("NEW TEACHER ADDED")

    except Exception as E:
        print("ERROR DURING INSERTION")
    finally:
        if conn:
            dbConnection.close(conn)        