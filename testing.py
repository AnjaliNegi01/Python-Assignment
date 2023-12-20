import unittest
from dao.addStudents import addStudents
from dao.displayStudentInfo import displayStudentInfo

class MyTestCase(unittest.TestCase):

    def testaddStudent(self):
        # Create a lease
        newStudent = addStudents()
        studentlist = displayStudentInfo()
        # Check if the created lease is in the lease history
        if newStudent is not None:
            for i in studentlist:
                studentFound = any(newStudent[0][0] == i[0])
            self.assertTrue(studentFound)

if __name__ == '__main__':
    unittest.main()
