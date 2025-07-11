"""#variables/identifier 
item="apple" #string
price=20 #integers are whole number
price2=10.0 #float are decimal point numbers
boolean=True #boolean value

print("the item is",item) #printing the variable with a sentence
print("the price of", item, "is", price)"""

"""#to see the data type of  variable
item="apple" 
price=20
print(type(item))
print(type(price))"""

"""#Multiple variable assignment - assigning multiple values to different variables at once or a single value to different variables at once
Type1, Type2, Type3 = "Dum Biryani", "Hyd Biryani", "Lucknowi Biryani"
print(Type1)
#single value to multiple varaibles
Type1 = Type2 = Type3 = "Dum biryani"
print(Type1, Type2, Type3)

#taking input from user and defining datatype of input
name=str(input("Enter your name"))
print("My name is",name)
print(type(name))

age=int(input("Enter your age"))
print("My age is",age)
print(type(age))

marks= float(input("Enter your marks"))
print("Your marks is",marks)
print(type(marks))"""

list=[1,2,3,4,5]
if 6 in list:
    print("yes")
else:
    print("no")



