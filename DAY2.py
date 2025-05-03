#type casting
x=str(30)
print(x)
print(type(x))

#string slicing
item="apple" #n-1
print(item[0:5])
print(len(item))
print(item[2:5]) #[Upperbound:Lowerbound]
print(item[:5])
print(item[1:])
print(item[-5:])

fruit=item[6:]
print(fruit)

print(item.upper())
print(item.lower())
print(item.capitalize())
a = "With six children in tow, Catherine raced to the airport departing gate. This wasn't an easy task as the children had other priorities than to get to the gate. She knew that she was tight on time and the frustration came out as she yelled at the kids to keep up. They continued to test her, pretending not to listen and to move in directions that only slowed them down. They had no idea the wrath they were about to receive when Catherine made it to the gate only to be informed that they had all missed the plane."
print(a.split(","))

sentence="is a fruit and price is"
print(item +" "+ sentence)

#formatted strings
price=20
print(f"{item} {sentence} {price}")

Age = 20
Txt = f"My name is khushi and im {Age} years old"
print(Txt)


#operators
number= 2**3
print(number)

print(2+3)
print(2-3)
print(10/2)
print(10//2)
print(10%2)
print(10*2)
print(10**2)


string1 = "Hello World"
#string1 += " World"
#print(string1)
# Output: Hello World
#string1 = string1 + "world"
number = 3
number -= 5
print(number)

list=[1,2,3,4,5,5]
print(list)
print(6 in list)
print(6 not in list)

#BODMAS
