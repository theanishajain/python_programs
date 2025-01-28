a = [1,3,6,7,23,1,49,9,4,]

t = 7
left = 0
right= len(a)-1
a.sort()
print(a)
while left<right:
    
    if a[left] + a[right] == t:
        print(left,right)
        break
    elif a[left] + a[right] < t:
        left+=1
    else:
        right-=1