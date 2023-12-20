from util.DBConnUtil import dbConnection
def getPaymentHistory():
    try:
        conn,stmt=dbConnection.open()
        stmt.execute('''SELECT * FROM Payment''')
        record=stmt.fetchall()
        for i in record:
            print(i)
    except Exception as E:
        print(f"ERROR IN RETRIVAL {E}")
    finally:
        if conn:
            dbConnection.close(conn)