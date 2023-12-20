from util.DBConnUtil import dbConnection
def createTables():
    conn=None
    try:
        conn,stmt=dbConnection.open()
        if conn:
            stmt.execute('''CREATE TABLE if not exists Student (StudentID INT PRIMARY KEY,
                            FirstName VARCHAR(30),
                            LastName VARCHAR(30),
                            DateOfBirth DATE,
                            Email VARCHAR(30),
                            PhoneNumber CHAR(10))''')

            stmt.execute('''CREATE TABLE if not exists Teacher (TeacherID INT PRIMARY KEY,
                            FirstName VARCHAR(30),
                            LastName VARCHAR(30),
                            Email VARCHAR(30))''')

            stmt.execute('''CREATE TABLE if not exists Course (CourseID INT PRIMARY KEY,
                            CourseName VARCHAR(30),
                            Credit INT,
                            TeacherID INT,
                            FOREIGN KEY (TeacherID) REFERENCES Teacher (TeacherID))''')

            stmt.execute('''CREATE TABLE if not exists Enrollment (EnrollmentID INT PRIMARY KEY,
                            StudentID INT,
                            CourseID INT,
                            EnrollmentDate DATE,
                            FOREIGN KEY (StudentID) REFERENCES Student (StudentID),
                            FOREIGN KEY (CourseID) REFERENCES Course (CourseID))''')

            stmt.execute('''CREATE TABLE if not exists Payment (PaymentID INT PRIMARY KEY,
                            StudentID INT,
                            Amount DECIMAL(10,2),
                            PaymentDate DATE,
                            FOREIGN KEY (StudentID) REFERENCES Student (StudentID))''')
    except Exception as E:
         print(f"Error during database initialization: {E}")
            
            
    finally:
        if conn:
             dbConnection.close(conn)                