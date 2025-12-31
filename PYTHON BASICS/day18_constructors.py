# Day 18: Constructors and Instance Variables
# Topics:
# __init__, instance variables, methods

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Creating objects with data
student1 = Student("Vansh", 20, "BTech")
student2 = Student("Aman", 21, "BSc")

student1.display_info()
print("-----")
student2.display_info()
