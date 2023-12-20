from util.DBConnUtil import dbConnection
from exception.studentNotFound import StudentNotFoundException
from exception.paymentValidate import PaymentValidationException
def makePayments():
    PaymentID=int(input("Enter Payment ID: "))
    StudentID=int(input("Enter Student ID: "))
    Amount=float(input("Enter Amount: "))
    PaymentDate=input("Enter Payment Date: ")
    try:
        conn,stmt=dbConnection.open()
        # Validate payment amount
        PaymentValidationException.validate_payment_amount(Amount)

        # Check if the student is not found
        if not StudentNotFoundException.is_student_exists(StudentID, conn, stmt):
            raise StudentNotFoundException()
        data=[(PaymentID,StudentID,Amount,PaymentDate)]
        stmt.executemany('''INSERT INTO Payment(PaymentID,StudentID,Amount,PaymentDate)
                            VALUES(%s,%s,%s,%s)''',data)
        conn.commit()
        print("NEW PAYMENT ADDED")
    except PaymentValidationException as pe:
        print(f"ERROR DURING MAKING PAYMENT: {pe}")
    except StudentNotFoundException as se:
        print(f"ERROR: {se}")
    except Exception as E:
        print("ERROR DURING MAKING PAYMENT")
    finally:
        if conn:
            dbConnection.close(conn)