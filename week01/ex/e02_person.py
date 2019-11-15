class Person:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def introduce(self):
        print(f"Hi, my name is {self.name}.")