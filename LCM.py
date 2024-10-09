'''LCM: maximum of two numbers could be a*b
LCM: a*b is always divisible by a and b
LCM: smallest can be max(a,b) 
LCM: smallest number may divide the larger one than that will become the
least common multiple'''
n1= int(input())
n2= int(input())
larger_number = n1 if n1>n2 else n2
while larger_number<=n1*n2:
    if larger_number%n1==0 and larger_number%n2==0:
        print(larger_number)
        break
    larger_number+=1