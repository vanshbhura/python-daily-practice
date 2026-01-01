# Day 19: Inheritance
# Topics:
# parent class, child class, code reuse

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, course):
        Person.__init__(self, name, age)
        self.course = course

    def show_student_info(self):
        self.show_info()
        print("Course:", self.course)

# Creating object of child class
student = Student("Vansh", 20, "BTech")
student.show_student_info()
