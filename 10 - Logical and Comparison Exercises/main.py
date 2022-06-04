# Logical and Comparison Exercises
# Make simple program that can be used as slice and combine number


# First Exercise: 
# Check if the number beetween 0 and 5, or beetween 8 and 11
number = float(input("Enter the number that:\nbeetween 0 and 5\nand\nbeetween 8 and 11\n:"))

# Check input number that qualify the requirement
a   = ((number > 0) and (number < 5)) or ((number > 8) and (number < 11))
print("The number ",number, "is", a, "and qualified the requirements")

# Separator
print('\n',20*'=','\n')

# Second Exercise: 
# Check if the number less than 0 and more than 5, or less than 8 and more than 11
number = float(input("Enter the number that:\nless than 0 and more than 5\nor\nless than 8 and more than 11\n:"))

# Check input number that qualify the requirement
b   = (number < 0) or ((number > 5) and (number < 8)) or (number > 11)
print("The number ",number, "is", b, "and qualified the requirements")