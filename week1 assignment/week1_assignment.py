

# Task 1: Convert between different data types

print("=" * 10)
print("Task 1: Convert between different data types")
print("=" * 10)


float_value = 3.75
int_value = int(float_value)
print(f"Data type: {type(int_value)}")
print()


string_value = "123"
float_value = float(string_value)
print(f"Data type: {type(float_value)}")
print()


zero_value = 0
bool_value = bool(zero_value)
print(f"Data type: {type(bool_value)}")
print()

# Convert False to a string and print the value
bool_false = False
string_value = str(bool_false)
print(f"Data type: {type(string_value)}")
print()


# Task 2: Convert all characters in the string to uppercase

print("=" * 10)
print("Task 2: Convert string to uppercase")
print("=" * 10)

x = "hello"
uppercase_x = x.upper()
print(f"Uppercase string: {uppercase_x}")
print()

# Task 3: Calculate z = x + y and determine data type, then convert to integer
print("=" * 10)
print("Task 3: Calculate z = x + y, check type, and convert to integer")
print("=" * 10)

x = 5
y = 3.14
z = x + y

print(f"x = {x} (type: {type(x)})")
print(f"y = {y} (type: {type(y)})")
print(f"z = x + y = {z}")
print(f"Data type of z: {type(z)}")

z_int = int(z)
print(f"Data type after conversion: {type(z_int)}")
print()

# Task 4: String operations on 'hello'
print("=" * 10)
print("Task 4: String operations on 'hello'")
print("=" * 10)

s = 'hello'

uppercase_s = s.upper()
print(f"1. Convert to uppercase: {uppercase_s}")
print()

# Replace 'e' with 'a'
replaced_s = s.replace('e', 'a')
print(f"2. Replace 'e' with 'a': {replaced_s}")
print()

# Check if the string starts with 'he'
starts_with_he = s.startswith('he')
print(f"3. Check if string starts with 'he': {starts_with_he}")
print()

# Check if the string ends with 'lo'
ends_with_lo = s.endswith('lo')
print(f"4. Check if string ends with 'lo': {ends_with_lo}")
print()



