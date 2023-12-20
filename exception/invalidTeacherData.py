class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid Teacher data"):
        self.message = message
        super().__init__(self.message)
    def validate_email(email):
        if "@" not in email or "." not in email:
            return False