import random

class NumberEncryptor:
    def __init__(self):
        self.encrypted_number = None

    def encrypt(self, number):
        self.encrypted_number = number
        self._perform_random_operation()

    def decrypt(self):
        self._perform_random_operation(inverse=True)
        return self.encrypted_number

    def _perform_random_operation(self, inverse=False):
        operation = random.choice(['add', 'subtract', 'multiply'])
        operand = random.randint(1, 10)

        if operation == 'add':
            self.encrypted_number += operand if not inverse else -operand
        elif operation == 'subtract':
            self.encrypted_number -= operand if not inverse else -operand
        elif operation == 'multiply':
            self.encrypted_number *= operand if not inverse else 1/operand