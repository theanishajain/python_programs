# l1 = [1,5,6,4,6]
# print(l1.index(5)) if 5 in l1 else print('5 is not there')
l =[]
for i in range(start, end+1):
    if i>1:
        for j in range(2,start):
            if i%j==0:
                print(i)
            else 