# Separate the string into comma-separated values
X = "India.is.my.country"
separated_values = X.split(".")
comma_separated = ",".join(separated_values)
print(comma_separated)

#Remove a given character from a string
Y = "M.A.N.I.P.A.L"
character_to_remove = "A"
result = Y.replace(character_to_remove, "")
print(result)

#Remove dots (.) from the string
Y = "M.A.N.I.P.A.L"
result_without_dots = Y.replace(".", "")
print(result_without_dots)

#Sort strings alphabetically
strings = ["apple", "banana", "cherry", "date"]
strings.sort()
print(strings)

#Reverse the input string
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

#Check if a string contains only digits
input_string = input("Enter a string: ")
if input_string.isdigit():
    print("The string contains only digits.")
else:
    print("The string contains characters other than digits.")

#Find the number of vowels in a string
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in input_string if char in vowels)
print("Number of vowels:", vowel_count)

