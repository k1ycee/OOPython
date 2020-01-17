class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            print("Hired")

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print("Fired")

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev = Developer('Okoro', ' Chidubem', 25000, 'Go')
mgr = Manager('Francis', 'Rice', 100000, [dev])

print(mgr.mail)
mgr.print_emps()
mgr.remove_emp(dev)
mgr.print_emps()

