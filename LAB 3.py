# CODE for Disarium number

def is_disarium_number(num):
    num_str = str(num)
    total_sum = 0
    for i, digit in enumerate(num_str):
        total_sum += int(digit) ** (i + 1)
    return total_sum == num
num = int(input("Enter a number: "))
if is_disarium_number(num):
    print(f"{num} is a Disarium number.")
else:
    print(f"{num} is not a Disarium number.")

#code for harshad number

def is_harshad_number(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    return num % digit_sum == 0
num = int(input("Enter a number: "))
if is_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")

#code for nCr calculation

import math
def nCr(n, r):
    if r > n:
        return 0
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
n = int(input("Enter n: "))
r = int(input("Enter r: "))
result = nCr(n, r)
print(f"The value of {n}C{r} is {result}.")

#code for finding reverse of given number

def reverse_number(num):
    return int(str(num)[::-1])
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}.")

#1
def pattern1():
    for i in range(1, 6):
        print(" ".join([str(i)] * i))
pattern1()

#2
def pattern2():
    for i in range(5, 0, -1):
        print(" " * (5 - i) + " ".join([str(i)] * i))
pattern2()

#3
def pattern3():
    for i in range(1, 6):
        print(" " * (5 - i) + " ".join([str(x) for x in range(1, i + 1)]))
pattern3()

#4
def pattern4():
    for i in range(5, 0, -1):
        print(" " * (5 - i) + " ".join([str(i)] * i))
pattern4()

#5
def pattern5():
    for i in range(5, 0, -1):
        print(" " * (5 - i) + " ".join(["5"] * i))
pattern5()

#6
def pattern6():
    for i in range(1, 6):
        print(" " * (5 - i) + " ".join([str(x) for x in range(i, 0, -1)]))
pattern6()

#7
def pattern7():
    for i in range(6, 0, -1):
        print(" ".join([str(x) for x in range(i)]))
pattern7()

#8
def pattern8():
    num = 1
    for i in range(1, 4):
        row = [str(x) for x in range(num, num + i)]
        print(" ".join(row))
        num = num + i
pattern8()

#9
def pattern9():
    num = 1
    for i in range(1, 5):
        row = [str(x) for x in range(num, num + i)]
        print(" ".join(row[::-1]))
        num = num + i

pattern9()

#10
def pattern10():
    for i in range(1, 6):
        row = [str(x) for x in range(1, i + 1)]
        row = row + row[-2::-1]
        print(" ".join(row))
pattern10()

#11
def pattern11():
    for i in range(5, 0, -1):
        row1 = " ".join([str(x) for x in range(5, i - 1, -1)])
        row2 = " ".join([str(x) for x in range(i, 6)])
        print(row1 + " " + row2)
pattern11()

#12
def pattern12():
    num = 10
    for i in range(1, 6):
        row = [str(num - 2 * j) for j in range(i)]
        print(" ".join(row))
        num -= 2
pattern12()

#13
def pattern13():
    for i in range(7):
        row = [str(i * j) for j in range(i + 1)]
        print(" ".join(row))
pattern13()

#14
def pattern14():
    num = 1
    for i in range(1, 6):
        row = [str(num) for j in range(i)]
        print(" ".join(row))
        num += 2
pattern14()

#15
def pattern15():
    for i in range(1, 6):
        print(" " * (5 - i) + " ".join([str(x) for x in range(1, i + 1)]))
pattern15()

#16
def pattern16():
    for i in range(1, 8):
        print(" " * (7 - i) + "* " * i)
pattern16()

#17
def pattern17():
    for i in range(6, 0, -1):
        print(" " * (6 - i) + "* " * i)
pattern17()

#18
def pattern18():
    for i in range(1, 6):
        print(" " * (5 - i) + "* " * i)
pattern18()