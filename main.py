from dao.createTables import createTables
from dao.addStudents import addStudents
from dao.updateStudent import updateStudentInfo
from dao.updateTeacherInfo import updateTeacherInfo
from dao.makePayment import makePayments
from dao.displayStudentInfo import displayStudentInfo
from dao.addTeacher import addTeacher
from dao.asignTeacher import assignTeacher
from dao.enrollInCourse import enrollInCourse
from dao.getEnrolledCourse import getEnrolledCourse
from dao.getPaymentHistory import getPaymentHistory
from dao.displayCourseInfo import displayCourseInfo
from dao.getEnrollment import getEnrollment
from dao.getTeacher import getTeacher
from dao.displayTeacherInfo import displayTeacherInfo
from dao.getStudent import getStudent
from dao.getAssignedCourses import getAssignedCourses
from dao.getstudentForPayment import getStudentForPayment
if __name__=="__main__":
    try:
        print("\n\nEnter 1 to add new Student")
        print("\nEnter 2 to update student Info")
        print("\nEnter 3 to make new Payment")
        print("\nEnter 4 to display students")
        print("\nEnter 5 to add new Teacher")
        print("\nEnter 6 to assign teacher to course")
        print("\nEnter 7 to enroll student in course")
        print("\nEnter 8 to get enrolled course")
        print("\nEnter 9 to get Payment History")
        print("\nEnter 10 to display Course Information")
        print("\nEnter 11 to get enrolled students")
        print("\nEnter 12 to get assigned teacher for course")
        print("\nEnter 13 to display teacher Information")
        print("\nEnter 14 to get student")
        print("\nEnter 15 to get list of Courses assiged to teacher")
        print("\nEnter 16 to Retrieve students associated with the payment")
        print("\nEnter 17 to update teacher info")
        print("\nEnter 18 to exit")
        while True:
            c=input("\nEnter choice: ")
            if c=='1':
                addStudents()
            elif c=='2':
                updateStudentInfo()
            elif c=='3':
                makePayments()
            elif c=='4':
                displayStudentInfo()
            elif c=='5':
                addTeacher()
            elif c=='6':
                assignTeacher()
            elif c=='7':
                enrollInCourse()
            elif c=='8':
                getEnrolledCourse()
            elif c=='9':
                getPaymentHistory()
            elif c=='10':
                displayCourseInfo()
            elif c=='11':
                getEnrollment()
            elif c=='12':
                getTeacher()
            elif c=='13':
                displayTeacherInfo()
            elif c=='14':
                getStudent()
            elif c=='15':
                getAssignedCourses()
            elif c=='16':
                getStudentForPayment()
            elif c=='17':
                updateTeacherInfo()
            elif c=='18':
                break
            else:
                print("Invalid choice")
    except Exception as E:
        print(f"\nAn error has occured: {E}")