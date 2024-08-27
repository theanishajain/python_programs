from array import *
a1 = array('i', [1, 3, 4])
print(a1)
print(type(a1))

def get_index(tup, elem):
    
    
    # YOUR CODE GOES HERE
    for index, value in enumerate(tup):
        if value == elem:
          return index
    return -1
# Que2. Write a program to divide a given tuple into two tuples that contain even and odd indexed elements of the original tuple. Print both these tuples in the given output format.

# Note: The input tuple follows 1-based indexing. This means the element at index 0  is treated as having index as 1. 

# For example, (9,2,3). The 1-based index of 2 is 2.

# Input Format:

# The input contains a tuple as an argument to the function.
# Output Format:

# Print two tuples one for odd indexed elements and another for even indexed elements in the following format:
# Odd: (....)
# Even: (....)
# Sample Input:

# 1
# (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
# Sample Output:

# Odd: (10, 5, 10, 10, 5, 8)
# Even: (8, 2, 15, 8, 8, 2)
def odd_even_split_tuple(tup):
    ''' input:tup-indicates the tuple
         output:print two tuples one for even indexed and odd indexed in the given output format'''
    
    # YOUR CODE GOES HERE
    

    odd_elements = tup[0::2]
    even_elements = tup[1::2] 
    print("Odd:", odd_elements )
    print("Even:", even_elements)

