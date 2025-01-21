"""
 * * *   * * *
 * *       * *
 *           *
 * *       * *
 * * *   * * *
    """
n = int(input())
row = 1
nst = 3
nsp = 1
while(row<= n):
    for i in range(1,nst+1):
        print("*", end = "")
    for i in range(1,nsp+1):
        print(" ", end = "")
    for i in range(1,nst+1):
        print("*",end = "")
    print()
    if row<=n/2:
        nst = nst - 1
        nsp = nsp  + 2
    else:
        nst = nst + 1
        nsp = nsp - 2
    row = row + 1
        