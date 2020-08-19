# Discussion Questions: 
# 1. Construct a class hierarchy for people on a college campus. 
# Include faculty, staff, and students. What do they have in common? 
# What distinguishes them from one another?

# Good in depth resources for .super()
# https://realpython.com/python-super/


class Person:

    def __init__(self, name, start_date, stop_date):
        self.name = name
        self.start_date = start_date
        self.stop_date = stop_date

    def get_name(self):
        return self.name

    def update_name(self, new_name):
        self.name = new_name
        return self.name


class Student(Person):

    def __init__(self, name, start_date, stop_date, tuition):
        super().__init__(name, start_date, stop_date)
        
        self.tuition = tuition
        self.enrolled = start_date
        self.graduated = stop_date

    def get_tuition(self):
        return self.tuition

    def get_attendace_record(self):
        print("Attended from", self.enrolled, self.graduated)

    
class Employee(Person):

    def __init__(self, name, start_date, stop_date, salary, position):
        super().__init__(name, start_date, stop_date)
        
        self.salary = salary
        self.position = position

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

    def apply_raise(self):
        self.salary = self.salary + (self.salary * .2)
        return self.salary


person = Person('laura', 'June 19', 'Oct 18')
student = Student('sara', 'Nov 3', 'Jul 5', 50000)
employee = Employee('joe', 'Jan 4', 'Mar 9', 78000, 'teacher')