class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.mail)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


p1 = Employee('Corey', 'Honda', 40000)
p2 = Employee('Corey', 'Honda', 60000)

print(p1 + p2)