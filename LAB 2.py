#code for fibonacci series using loops

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Enter the number of terms: "))
fibonacci(n)

#for factorial using loop

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is {factorial(n)}")

#to check given code is armstrong or not

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n
n = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

#perfect number check

def is_perfect_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
n = int(input("Enter a number to check if it's a perfect number: "))
if is_perfect_number(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

#print multiplication table

def print_multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")
n = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(n)

#calculate LCM and GCD of two number

import math
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd_value = math.gcd(a, b)
lcm_value = lcm(a, b)
print(f"GCD of {a} and {b} is: {gcd_value}")
print(f"LCM of {a} and {b} is: {lcm_value}")