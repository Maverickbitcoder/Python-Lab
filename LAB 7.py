#Create a Person class with name and age attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")

#Create a Student class with a name and roll_no attribute.
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
student = Student("John", 2)
print(f"Name: {student.name}, Roll No: {student.roll_no}")

#Define a BankAccount class with methods to deposit, withdraw, and check balance.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print(f"Current balance: {self.balance}")
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()

#Define a Student class with name and age attributes, and create objects for different students.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
print(f"Name: {student1.name}, Age: {student1.age}")
print(f"Name: {student2.name}, Age: {student2.age}")


# Define the ComplexNumber class
import math
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def add(self, c):
        real_sum = self.real + c.real
        imaginary_sum = self.imaginary + c.imaginary
        return ComplexNumber(real_sum, imaginary_sum)
    def magnitude(self):
        return math.sqrt(self.real**2 + self.imaginary**2)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i" if self.imaginary >= 0 else f"{self.real} - {-self.imaginary}i"
complex1 = ComplexNumber(3, 4)  # 3 + 4i
complex2 = ComplexNumber(1, 2)  # 1 + 2i
sum_complex = complex1.add(complex2)
print(f"Complex Number 1: {complex1}")
print(f"Complex Number 2: {complex2}")
print(f"Sum: {sum_complex}")
print(f"Magnitude of Complex Number 1: {complex1.magnitude()}")
print(f"Magnitude of Complex Number 2: {complex2.magnitude()}")
print(f"Magnitude of Sum: {sum_complex.magnitude()}")

#Person and Student Classes (Single Inheritance)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")
student = Student("John Doe", 20, "S12345")
student.show_details()

#Vehicle, Car, and ElectricCar Classes (Multilevel Inheritance)
class Vehicle:
    def info(self):
        print("This is a vehicle")
class Car(Vehicle):
    def car_info(self):
        print("This is a car")
class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery.")
electric_car = ElectricCar()
electric_car.info()
electric_car.car_info()
electric_car.battery_info()

#Teacher, Author, and TutorAuthor Classes (Multiple Inheritance)
class Teacher:
    def description(self):
        print("I am a teacher.")
class Author:
    def description(self):
        print("I am an author.")
class TutorAuthor(Teacher, Author):
    def description(self):
        super().description()
        print("I am also a tutor-author.")
tutor_author = TutorAuthor()
tutor_author.description()

# Animal, Dog, and Cat Classes (Hierarchical Inheritance)
class Animal:
    def sound(self):
        print("Animals make sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()