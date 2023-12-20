class CourseNotFoundException(Exception):
    def __init__(self, message="Course not found"):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def is_course_exists(course_id, conn, stmt):
        stmt.execute('SELECT 1 FROM Course WHERE CourseID = %s', (course_id,))
        return bool(stmt.fetchone())