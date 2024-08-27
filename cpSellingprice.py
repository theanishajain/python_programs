cp = int(input("Enter cost price"))
sp = int(input("Enter selling price"))
if sp > cp:
    print("Seller made profit")
elif sp == cp:
    print("Seller made no profit or no Loss")
else:
    print("Seller made loss")