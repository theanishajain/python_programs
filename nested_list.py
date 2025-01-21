num = int(input("Enter the numbers of lists you want into a list"))
final_list = []
for i in range(num):
    l = [int(x) for x in input("Enter the elements of the list").split() ]
    final_list.append(l)
print(final_list)