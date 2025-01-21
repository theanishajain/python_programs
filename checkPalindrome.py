##Special Code

# l = [[1,3,5,55],[3,6,7],[3,6,77]]
# print(len(l))
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         # print(len(i))
#         print(l[i][j])

##Palindrome Program
string = "MAM"
first = 0
Second = len(string) - 1
status = 1

while first < Second:
    if string[first] == string[Second]:
        first = first + 1
        Second = Second - 1
    else:
        status = 0
        break  # Break the loop as soon as a mismatch is found

if status == 1:
    print("String is palindrome")
else:
    print("String is not palindrome")