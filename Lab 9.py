#lab 9
#The try and except Block to Handling Exceptions
#1
try:
    a = 10
    b = 0
    c = a / b
    print("The answer of a divided by b:", c)
except ZeroDivisionError:
    print("Can't divide by zero. Please provide a different number.")
#2
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print("The answer of a divided by b:", c)
except ValueError:
    print("Entered value is not a valid integer.")
except ZeroDivisionError:
    print("Can't divide by zero.")

#Handle multiple exceptions with a single except clause
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print("The answer of a divided by b:", c)
except (ValueError, ZeroDivisionError):
    print("Please enter a valid value. Make sure b is not zero.")

#Using try with finally
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print("The answer of a divided by b:", c)
except ZeroDivisionError:
    print("Can't divide by zero.")
finally:
    print("Inside the finally block.")

#Using try with else clause
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print("a/b = %d" % c)
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print("We are in the else block.")

#Raising an Exception
def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)
        interest = (amount * year * rate) / 100
        print('The Simple Interest is', interest)
        return interest
    except ValueError:
        print('Interest rate is out of range:', rate)
print('Case 1')
simple_interest(800, 6, 8)
print('Case 2')
simple_interest(800, 6, 800)

#Exception Chaining
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = a / b
    print("The answer of a divided by b:", c)
except ZeroDivisionError as e:
    raise ValueError("Division failed") from e

#Custom and User-defined Exception

class ValueTooSmallError(Exception):
    """Exception raised when the value is too small."""
    pass

class ValueTooLargeError(Exception):
    """Exception raised when the value is too large."""
    pass

while True:
    try:
        num = int(input("Enter any value in the range of 10 to 50: "))
        if num < 10:
            raise ValueTooSmallError
        elif num > 50:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value is below range.. try again.")
    except ValueTooLargeError:
        print("Value is out of range.. try again.")

print("Great! Value is within the correct range.")

#Exception Life Cycle

def sum_of_list(numbers):
    return sum(numbers)

def average(total_sum, n):
    # Handle ZeroDivisionError if the list is empty
    if n == 0:
        return 0
    return total_sum / n

def final_data(data):
    for item in data:
        print("Average:", average(sum_of_list(item), len(item)))

list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400, 500]
list3 = []  # empty list
lists = [list1, list2, list3]

