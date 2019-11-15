class Person:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.tup = (firstname,lastname)
    def get_info(self):
        return self.tup
    def introduce(self):
        print(f"Hello! my name is {self.firstname} {self.lastname}, I am a Person")
class Student(Person):
    def introduce(self):
        print(f"Hello! my name is {self.firstname} {self.lastname}, I am a Student")
class Teacher(Person):
    def introduce(self):
        print(f"Hello! my name is {self.firstname} {self.lastname}, I am a Teacher")