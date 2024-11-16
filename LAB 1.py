#code for check prime number or not

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#code to find given number is palindrome or not

def is_palindrome(number):
    return str(number) == str(number)[::-1]
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#if number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"{num} is {result}.")

#code to find the grade of student using percentage

def find_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "F"
percentage = float(input("Enter the percentage: "))
if 0 <= percentage <= 100:
    grade = find_grade(percentage)
    print(f"The grade for {percentage}% is: {grade}")
else:
    print("Invalid percentage. Please enter a value between 0 and 100.")

#code for simple console calculator

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input! Please select a valid operation.")

#code to check wether given code is armstrong number or not

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#To find the sum of digits

def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number = number // 10
    return total
num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"The sum of the digits of {num} is: {result}")

# To check wether number is perfect number or not

def is_perfect_number(number):
    if number <= 1:
        return False
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == number
num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

#code to reverse a number

def reverse_number(number):
    reversed_num = 0
    while number > 0:
        last_digit = number % 10
        reversed_num = reversed_num * 10 + last_digit
        number = number // 10
    return reversed_num
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"The reversed number is: {reversed_num}")

#code to check for strong number

import math
def is_strong_number(number):
    digits = str(number)
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    return sum_of_factorials == number
num = int(input("Enter a number: "))
if is_strong_number(num):
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong Number.")

#calculate area of circle

import math
def area_of_circle(radius):
    return math.pi * (radius ** 2)
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")

#code for factorial of number
import math
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    else:
        return math.factorial(number)
num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is: {result}")

#code for factorial 1 to 50

import math
for num in range(1, 51):
    factorial_value = math.factorial(num)
    print(f"The factorial of {num} is: {factorial_value}")

#    code for fibonacci series till 10

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
n = 10
fib_sequence = fibonacci(n)
print(f"Fibonacci series up to the {n}th number: {fib_sequence}")

#for sum of fibonacci

def fibonacci_sum(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return sum(fib_series)
n = 10
fib_sum = fibonacci_sum(n)
print(f"The sum of the Fibonacci series up to the {n}th number is: {fib_sum}")