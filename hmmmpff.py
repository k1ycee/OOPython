class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('AH THAT ONE IS DONE')
        self.first = None
        self.last = None


r = Employee('gbera', 'ojkweu')
r.fullname = 'utI gbain'
del r.fullname
print(r.mail)
print(r.fullname)
# print(r.)