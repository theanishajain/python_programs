# a = [3,5,6,7,2]

# new_list = []

# while a:
#  smaller = a[0]
#  for i in range(1,len(a)):
#     if smaller > a[i]:
#         smaller = a[i]
#         new_list.append(smaller)
#         a.remove(smaller)
# print(new_list)
        
a = [3, 5, 6, 7, 2]
new_list = []  # List to store sorted elements

while a:  # Repeat until the original list is empty
    smaller = a[0]  # Assume the first element is the smallest
    for i in range(1, len(a)):  # Compare with the remaining elements
        if a[i] < smaller:
            smaller = a[i]  # Update the smallest element
    new_list.append(smaller)  # Add the smallest element to the new list
    a.remove(smaller)  # Remove the smallest element from the original list

print(new_list)
