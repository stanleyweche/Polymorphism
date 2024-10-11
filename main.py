class Person:
    def __init__(self, fname, sname, lname):
        self.first = fname
        self.second = sname
        self.last = lname

    def myfunc(self):
        return f"My name is {self.first} {self.second}"

    # Property to get the full name
    @property
    def fullname(self):
        return f"{self.first} {self.second} {self.last}"

    # Method to change the last name
    def change_last_name(self, new_last_name):
        self.last = new_last_name

parent = Person('John', 'Doe', 'JD')
print(parent.myfunc())
print(parent.fullname)

class Student(Person):
    def __init__(self, fname, sname, lname, student_id):
        super().__init__(fname, sname, lname)
        self.student_id = student_id

    def myfunc(self):
        return f"I am a student, my name is {self.first} {self.second}, ID: {self.student_id}"

    # Property to get the student details
    @property
    def details(self):
        return f"Name: {self.fullname}, ID: {self.student_id}"

student1 = Student('Mary', 'Doe', 'Kali', 'S12345')
print(student1.myfunc())
print(student1.details)

# Demonstration of polymorphism
people = [parent, student1]

for person in people:
    print(person.myfunc())
