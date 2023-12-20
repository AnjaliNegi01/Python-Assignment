from util.DBConnUtil import dbConnection
def getPaymentAmount():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT PaymentID,Amount from Payment''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR DURING RETRIVAL {E}")
    finally:
        if conn:
            dbConnection.close(conn)