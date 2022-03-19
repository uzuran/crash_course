import datetime


class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_rise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def its_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->',  emp.fullname())



my_date = datetime.datetime.now()
print(Employee.its_workday(my_date))


dev_1 = Developer('Corey', 'Schafer', 5000, 'Python')
emp_2 = Employee('Test', 'User', 6000)

mgr1 = Manager('Artom', 'Cernopascenko', 90000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-70000'
emp_str_3 = 'Jane-Doe-70000'



new_emp = Employee.from_string(emp_str_1)

print(new_emp.email)

print(mgr1.email)

mgr1.add_emp(mgr1)
mgr1.add_emp(dev_1)

mgr1.print_emps()

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

mgr1.print_emps()



