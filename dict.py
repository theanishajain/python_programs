d = {104 : 'Anisha', 105:"Akshat"}
print(d.items())#gonna return in tuple format
#unpacking of tuple
for k,v in d.items():
    print(k,v)
#And another way of printing dictionary
for i in d.items():
    k=i[0]
    v=i[1]
    print(k,v)
    
#dict Comprehension
d1 = {a:a**2 for a in range(1,8,1)}
print(d1)
    