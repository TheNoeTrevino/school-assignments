# Part 1: Basic Python Syntax (2 pts.)
#
#     Create a variable, var, and set the value to the string Hello, world!.
#         Now print the length of var.
#         Extract world from var using string index slicing.
#     Print the types for 1, 1.0, and “1” and note how they differ.
#     Calculate and print the area of a circle of radius 5 to two decimal places.
#     Write a for loop that prints all odd numbers from 9 to 21 including both numbers.
#     Write an if/else statement that takes a variable var and prints
#         Greater than 8 if var is greater than 8,
#         Less than 9 if var is less than 9,
#         Equal to 10 if var is equal to 10.
#
# Make sure to appropriately test for each case.
#
#     Write a function which takes a string as its parameter and returns the length of the string.
#     Write a function which takes a positive integer n as its parameter, and prints out all odd numbers from 1 to n.

var = "Hello, world!"
print(var[:7])
print(len(var))

print(type(1))
print(type(1.0))
print(type("1"))

for i in reversed(range(10)):
    print(i)

# TODO: how can we check if it is evenly divisible by 2?
for i in range(9, 22):
    if i % 2:
        print(i)


def greater_or_less(v):
    if v > 8:
        if v == 10:
            print("Value is 10")
        else:
            print("Greater than 8")

    if v < 9:
        print("Less than 9")


value = input("Enter an integer: ")

greater_or_less(int(value))

value = input("Enter a string: ")
print(len(value))


# TODO: Write a function which takes a positive integer n as its parameter, and prints out all odd numbers from 1 to n.
def all_previous_odds(value):
    for i in range(value):
        if i % 2 != 0:
            print(i)


all_previous_odds(10)
