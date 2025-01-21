"""    *
    *  *  *
 *  *  *  *  *
    *  *  *
       *      """
       
n = int(input())
row = 1
nsp = n//2
nst = 1
while (row<=n):
    for i in range(1,nsp+1):
        print(" ",end = " ")
    for i in range(1,nst+1):
        print("*", end = " ")
    print()
    if row<=n//2:
        nsp = nsp - 1
        nst = nst + 2
    else:
        nsp = nsp + 1
        nst = nst -2
    row= row + 1
        
        
    


      
