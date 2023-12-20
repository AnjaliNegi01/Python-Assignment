from util.DBConnUtil import dbConnection
def getStudentForPayment():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT S.StudentID,S.FirstName,S.LastName,P.PaymentId,P.Amount,P.PaymentDate FROM Payment as P
                        JOIN Student AS S ON  S.StudentID=P.StudentID''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR DURING INSERTION: {E}")
    finally:
        if conn:
            dbConnection.close(conn)