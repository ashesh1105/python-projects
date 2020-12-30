import requests

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay=0):
        self.first = first
        self.last = last
        self.pay = pay

    # Note: With @property decorator, you need to call email as <emp_object>.email and not .email()!
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    # Note: With @property decorator, you need to call email as <emp_object>.fullname and not .fullname()!
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.raise_amt * self.pay)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'