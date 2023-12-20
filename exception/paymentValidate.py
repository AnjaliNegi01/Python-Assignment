class PaymentValidationException(Exception):
    def __init__(self, message="Payment validation failed"):
        self.message = message
        super().__init__(self.message)
    @staticmethod
    def validate_payment_amount(amount):
        if amount <= 0:
            raise PaymentValidationException("Invalid payment amount")

