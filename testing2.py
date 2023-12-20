import unittest
from dao.addTeacher import addTeacher
from dao.displayTeacherInfo import displayTeacherInfo

class MyTestCase(unittest.TestCase):

    def testaddTeacher(self):
        # Create a lease
        newTeacher = addTeacher()
        teacherlist = displayTeacherInfo()
        # Check if the created lease is in the lease history
        if newTeacher is not None:
            for i in teacherlist:
                teacherFound = any(newTeacher[0][0] == i[0])
            self.assertTrue(teacherFound)

if __name__ == '__main__':
    unittest.main()