#Lists
color=['blue','green','red','yellow']
print(color)
print(color[1])
print(color[-1])
fruit = ['blueberry','apple','cherry','banana']
print(fruit)
print(fruit[1])

print(color[1],fruit[1])
print (color[0],fruit[0], color[1], fruit[1], color[2], fruit[2], color[3], fruit[3])

thislist = list() # note the double round-brackets
print(thislist)

print(color[1:3])
print(color[:3])
color[0]="black"
print(color)
color[1:3]=["pink","purple"]
print(color)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

color[1:3]=["navy blue"]
print(color)

color.insert(1,"red") #insert function takes index and value
print(color)

color.append("cyan") #add an item to the end of the list
print(color)

color.extend(fruit)  #to append elements from another list to the current list, use the extend()
print(color)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist)


color2=["blue","green","red","yellow"] #iterate using for loop
for i in range(len(color2)):
    print(color2[i])

thislist = ["apple", "banana", "cherry"] #iterate using list comprehension
[print(x) for x in thislist]

#for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print("mylist:",mylist)

thislist = ["apple", "banana", "cherry"]
mylist= list(thislist)
print("newlist:",mylist)

#list concatenation
thislist = ["apple", "banana", "cherry"]
thislist2 = ["blueberry","mango"]
print(thislist+thislist2)
#append function
for x in thislist2:
 print(thislist.append(x))
 print(thislist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


