s1 = input("Enter the integers separated by commas")
#split function always returns the list of strings
print(s1.split(','))
'''To print everything in a single line'''
lst = [int(x) for x in input("enter numbers separted by commas").split(',')]
print(lst)
