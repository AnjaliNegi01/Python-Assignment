class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found"):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def is_teacher_exists(teacher_id, conn, stmt):
        stmt.execute('SELECT 1 FROM Teacher WHERE TeacherID = %s', (teacher_id,))
        return bool(stmt.fetchone())