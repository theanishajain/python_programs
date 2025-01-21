start = int(input("Enter the starting number"))
end = int(input("Enter the ending number"))
l =[]
for i in range(start, end+1):
    if i>1:#1 is not a prime number
        for j in range(2,start):
            if i%j==0:
                break
            else :
                l.append(i)
    else:
        print("1 is not a prime number")
        break
print(l)
# print(f"Prime numbers {l}")