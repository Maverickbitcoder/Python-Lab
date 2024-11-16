#SINGLE INHERITANCE : EXAMPLE
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')
car = Car()
car.Vehicle_info()
car.car_info()

##MULTIPLE INHERITANCE : EXAMPLE

# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company:
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'Location:', location)

# Child class
class Employee(Person, Company):
    def employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create an object of Employee
employee = Employee()

# Access methods from both parent classes
employee.person_info("rk", 23)
employee.company_info("company", "sau polo")
employee.employee_info(800000, "python ")

# Create object of Employee
# Creating an Employee class instance
emp = Employee()

# Access data from both parent classes and the child class
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.employee_info(12000, 'Machine Learning')

##  HYBRID INHERITANCE

# Base class
class Vehicle:
    def vehicle_info(self):
        print('Inside Vehicle class')

# Child class inheriting from Vehicle
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class inheriting from Car (which makes it a multilevel inheritance)
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create an object of SportsCar
s_car = SportsCar()

# Access methods from all levels of inheritance
s_car.vehicle_info()    # Method from Vehicle class
s_car.car_info()        # Method from Car class
s_car.sports_car_info() # Method from SportsCar class

##Super

class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
        # Calling the superclass method using super() function
        c_name = super().company_name()
        print("Jessa works at", c_name)

# Creating an object of the child class
emp = Employee()
emp.info()

#

class Company:
    def fun1(self):
        print("Inside parent class")

class Employee(Company):
    def fun2(self):
        print("Inside child class.")

class Player:
    def fun3(self):
        print("Inside Player class.")

# Testing issubclass relationships
# Result: True
print(issubclass(Employee, Company))

# Result: False
print(issubclass(Employee, list))

# Result: False
print(issubclass(Player, Company))

# Result: True (since Employee is a subclass of Company)
print(issubclass(Employee, (list, Company)))

# Result: True (since Company is a subclass of itself)
print(issubclass(Company, (list, Company)))

#
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"Drawing a {self.color} shape"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"Drawing a {self.color} circle with radius {self.radius}"

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        return f"Drawing a {self.color} square with side length {self.side_length}"

# Creating instances of the derived classes
circle_instance = Circle("Red", 5)
square_instance = Square("Blue", 4)

# Accessing attributes and invoking methods
print(circle_instance.draw())  # Output: Drawing a Red circle with radius 5
print(square_instance.draw())  # Output: Drawing a Blue square with side length 4

##METHOD OVERRIDING

# Parent class
class Shape:
    data1 = "abc"  # properties

    def no_of_sides(self):  # function no_of_sides
        print("My sides need to be defined. I am from Shape class.")

    def two_dimensional(self):  # function two_dimensional
        print("I am a 2D object. I am from Shape class")

# Sub-class
class Square(Shape):
    data2 = "xyz"

    def no_of_sides(self):
        print("I have 4 sides. I am from Square class.")

    def color(self):
        print("I have teal color. I am from Square class.")

# Create an object of the Square class
sq = Square()
sq.no_of_sides()          # Override the no_of_sides of parent class
sq.two_dimensional()      # Inherit this method from the parent class
sq.color()                # It's own method - color

# Display and modify attributes
print("Old value of data1 =", sq.data1)
sq.data1 = "New value"    # Override property of the Parent class
print("The value of data1 in Shape class overridden by the Square class =", sq.data1)

##OVERRIDING IN MULTIPLE INHERITANCE

class Book:
    def subjectName(self):
        print("This is a generic Book")

    def aboutMe(self):
        print("Hi, I'm from Book!")

class Physics(Book):
    def subjectName(self):
        print("This is a Physics Book")

class Chemistry(Book):
    def subjectName(self):
        print("This is a Chemistry Book")

class Science(Physics, Chemistry):
    def subjectName(self):
        print("This is a Science Book")

# Create an object of the Science class
obj = Science()
obj.subjectName()  # Will execute the method from the class Science
obj.aboutMe()      # Will execute the method from the class Book