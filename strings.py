chai = "Lemon Chai"
print(chai)
first_char= chai[0]
print(first_char)
# slice.chai = chai[0:6]
# print(slice.chai)
 
 
num_list = "0123456789"
print(num_list[:]) #full result

print(num_list[3:]) #inclusive of start index , exclusive of end index
print(num_list[0:7:2]) #hopping to another element 
#0246 console

print(chai.replace("Lemon", "Ginger"))

#Convert string into list

str_to_list = "Lemon, Ginger, Masala, Mint"
print(str_to_list.split()) #by default
#['Lemon,', 'Ginger,', 'Masala,', 'Mint'] :console
str_save_int = " 1, lemon , -3"
print(str_save_int.replace("-3", "negative three"))
# print(type(str_save_int[0]))


#method find returns -1 if not found
print(chai.find("o"))


#way to convert list to string
chai_variety =[ "Lemon", "Masala", "Ginger"]
print("".join(chai_variety))
# LemonMasalaGinger
print(" ".join(chai_variety))

for letter in chai:
    print(letter)
    

chai ="He said, \"Masala chai is awesome\" "
print(chai)
# console: He said, "Masala chai is awesome" 



#Order format{}

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))



#raw string
name = "anisha\jain"
print(name)
name = "anisha\njain"
print(name)
name = r"anisha\njain"
print(name)

