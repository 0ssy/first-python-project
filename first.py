# This is a more comprehensive Python script with a greeting and a simple calculator.
# You can expand on this to add more features!

def greet_user(name):
    """
    This function takes a name as a string and prints a personalized greeting.
    """
    print(f"Hello, {name}! Welcome to your first expanded Python project.")
    print("-" * 40) # This adds a decorative line to separate the output

def add_two_numbers(num1, num2):
    """
    This function takes two numbers as arguments and returns their sum.
    """
    return num1 + num2

# --- Main Program Execution ---
# First, call the greeting function
user_name = "Jane"
greet_user(user_name)

# Now, let's use the new calculator function.
# We'll assign the result to a variable and print it.
number_a = 5
number_b = 7
total = add_two_numbers(number_a, number_b)

print(f"Let's add two numbers: {number_a} and {number_b}")
print(f"The sum is: {total}")

# You can experiment with different numbers here!
# For example, change 'number_a' and 'number_b' to other values.
# print(f"Another sum: {add_two_numbers(10, 25)}")
