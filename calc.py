# def add(num1,num2):
#     sum = num1 + num2
  
#     return sum


# def sub(num1, num2):
#     subtraction = num1 - num2
#     return subtraction

# def mul( num1, num2):
#     multi = num1 - num2
#     return multi

# def inp(n):
#     print(n)
N = int(input("Enter the number of elements: "))
my_list = []
for _ in range(N):
    element = int(input("Enter element: ")) # Convert to integer if needed
    my_list.append(element)

