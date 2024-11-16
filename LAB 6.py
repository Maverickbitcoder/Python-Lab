#CODE FOR using 5 inbuilt function of list
# Creating a list
my_list = [10, 20, 30, 40, 50]

# 1. append() - Adds an element to the end of the list
my_list.append(60)
print("After append:", my_list)

# 2. insert() - Inserts an element at a specified index
my_list.insert(2, 25)  # Inserting 25 at index 2
print("After insert:", my_list)

# 3. remove() - Removes the first occurrence of a specified element
my_list.remove(30)
print("After remove:", my_list)

# 4. pop() - Removes and returns the element at the specified index (default is the last element)
popped_element = my_list.pop()  # Popping the last element
print("After pop:", my_list)
print("Popped element:", popped_element)

# 5. sort() - Sorts the list in ascending order
my_list.sort()
print("After sort:", my_list)


#to pass the list as an argument in a function
def process_list(my_list):
    print("Original List:", my_list)
    my_list.append(100)
    print("After appending 100:", my_list)
    my_list.sort()
    print("After sorting:", my_list)
    return my_list
my_list = [40, 10, 20, 50, 30]
modified_list = process_list(my_list)
print("Modified List:", modified_list)

#code variable lenght argument in a function and perfrom cube of each element
def cube_of_elements(*args):
    cubes = []
    for num in args:
        cubes.append(num ** 3)
    return cubes
result = cube_of_elements(2, 3, 4, 5)
print("Cubes of the elements:", result)

#code that accept strings and calculate the number of uppercase and lowercase letters in a string
def count_case(string):
    uppercase_count = 0
    lowercase_count = 0
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    return uppercase_count, lowercase_count
input_string = "Hello World! This is Python."
upper, lower = count_case(input_string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")

#code for gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1 = 56
num2 = 98
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
