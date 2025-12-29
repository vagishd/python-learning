

from functools import reduce


# Exercise 1: Use map() to double each element of the given list

print("=" * 10)
print("Exercise 1: Double each element using map()")
print("=" * 10)

a = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, a))

print(f"Original list: {a}")
print(f"Doubled list: {doubled}")
print()


# Exercise 2: Use filter() and lambda to extract all even numbers

print("=" * 10)
print("Exercise 2: Extract even numbers using filter() and lambda")
print("=" * 10)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Original list: {numbers}")
print(f"Even numbers: {even_numbers}")
print()


# Exercise 3: Use reduce() and lambda to find the longest word

print("=" * 10)
print("Exercise 3: Find longest word using reduce() and lambda")
print("=" * 10)

words = ["apple", "banana", "cherry", "date"]

longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)

print(f"Original list: {words}")
print(f"Longest word: '{longest_word}'")
print()


# Exercise 4: Use map() to square each number and round to one decimal place

print("=" * 10)
print("Exercise 4: Square and round to one decimal place using map()")
print("=" * 10)

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]


squared_rounded = list(map(lambda x: round(x * x, 1), my_floats))

print(f"Original list: {my_floats}")
print(f"Squared and rounded: {squared_rounded}")
print()


# Exercise 5: Use filter() to select names with 7 or fewer characters

print("=" * 10)
print("Exercise 5: Select names with 7 or fewer characters using filter()")
print("=" * 10)

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]


short_names = list(filter(lambda name: len(name) <= 7, my_names))

print(f"Original list: {my_names}")
print(f"Names with 7 or fewer characters: {short_names}")
print()


# Exercise 6: Use reduce() to calculate the sum of all numbers

print("=" * 10)
print("Exercise 6: Calculate sum using reduce()")
print("=" * 10)

numbers_list = [1, 2, 3, 4, 5]


sum_result = reduce(lambda x, y: x + y, numbers_list)

print(f"Original list: {numbers_list}")
print(f"Sum of all numbers: {sum_result}")
print()


