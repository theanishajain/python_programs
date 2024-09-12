# To select only the different datatypes
l = [1, 2, 'a', 4, 'f']

# Use list comprehension with isinstance to filter integers
int_elements = [i for i in l if isinstance(i, int)]

# Print the list of integers
print(int_elements)


#Another code for the same in different way
l = [1, 2, 'a', 4, 'f']

# Initialize an empty list to store integers
int_elements = []

# Iterate through the list and check if each element is an integer
for i in l:
    if isinstance(i, int):
        int_elements.append(i)

# Print the list of integers
print(int_elements)


# &&&&&&   Tuple  Input&&&&&
# Taking input from user
user_input = input("Enter elements separated by commas: ")

# Split the input string by commas and convert it to a tuple
user_tuple = tuple(user_input.split(','))

# Print the resulting tuple
print("The tuple is:", user_tuple)

