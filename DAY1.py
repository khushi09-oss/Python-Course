#variables
item="apple" #string
price=20 #integer
price=10.0 #float
print("the item is",item) #printing the variable with a sentence
#to see the data type of  variable
print(type(item))
print(type(price))

#Multiple variable assignment - assigning multiple values to different variables at once or a single value to different variables at once
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
print(type(marks))




