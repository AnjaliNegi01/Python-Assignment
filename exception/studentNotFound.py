class StudentNotFoundException(Exception):
    def __init__(self, message="Student not found"):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def is_student_exists(StudentID, conn, stmt):
        stmt.execute('SELECT 1 FROM Course WHERE CourseID = %s', (StudentID,))
        return bool(stmt.fetchone())