matrix = [
    [1,2,3,4],
    [4,5,6,4],
    [88, 93 , 55,4]
    ]

transposed = []
for i in range(4):
    lst = []
    for row in matrix:
        lst.append(row[i])
    transposed.append(lst)
print(transposed)

# for i in matrix:
#     print(i)
    