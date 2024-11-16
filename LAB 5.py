# CODE to triple all number in a given list of integer
def triple_numbers(numbers):
    return [num * 3 for num in numbers]
numbers = [1, 2, 3, 4, 5]
tripled_numbers = triple_numbers(numbers)
print(tripled_numbers)

# To add three givn lists using map and lambda
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))
print(result)

# To listify the list of given string individually
strings = ["apple", "banana", "cherry"]
listified_strings = [list(s) for s in strings]
print(listified_strings)

#square three element of the list using map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

#to add the given list and find diffrence
numbers = [10, 5, 2, 8, 3]
sum_of_numbers = sum(numbers)
difference_of_numbers = numbers[0] - sum(numbers[1:])
print("Sum:", sum_of_numbers)
print("Difference:", difference_of_numbers)

#to convert a list of integer and tuple of integer into a list of strings
int_list = [1, 2, 3, 4]
int_tuple = (5, 6, 7, 8)
str_list = list(map(str, int_list)) + list(map(str, int_tuple))
print(str_list)

#to create a new list by taking specific elements from a tuple and converting a string value to an integer
tuple_data = ('10', '20', '30', '40', '50')
indices = [1, 3, 4]
new_list = [int(tuple_data[i]) for i in indices]
print(new_list)

#to compute the square of the first N fibonacci numbers
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence
def square_fibonacci(n):
    fib_sequence = fibonacci(n)
    return [x ** 2 for x in fib_sequence]
n = 10
squared_fibonacci = square_fibonacci(n)
print(squared_fibonacci)