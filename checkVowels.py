vowels = "aeiou"
str1 = "The quick brown fox jumps over the lazy dog"
add = ""
for i in str1:
    for j in vowels:
         if j == i:
          add = add + i
        # print(add)
            
        
print(add, sep="\n")
name = "Anisha Jain" + "AN"
print(name, sep="-")
print("Anisha", "Jain", sep = " ** ")