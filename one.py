def print_numbers(n):
    if n == 0: 
        return

    print_numbers(n - 1)  


print_numbers(5)

def factorial(n):

    if n == 0 or n == 1: 
        return 1



class Student:

    def display(self):
        print("Hello, I am a student")


# Object creation
s1 = Student()

# Calling method
s1.display()


class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Student Details")
        print("----------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def update_course(self, new_course):
        self.course = new_course
        print("Course updated successfully!")


# Creating objects
student1 = Student("Manhar", 23, "BCA")
student2 = Student("Rahul", 22, "BSc")

# Calling methods
student1.display_details()

print()

student2.display_details()

print()

student1.update_course("Python Full Stack")
student1.display_details()