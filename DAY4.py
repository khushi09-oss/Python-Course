mytuple=("apple","banana")
print(type(mytuple))


tuple=("apple",)
print(type(tuple))

"""x = ("apple", "banana", "cherry")
y = list(x) #list function
y[1] = "blackcurrant"
x = tuple(y)"""

#concatenation
"""thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #thistuple = thistuple+ y
print(thistuple)"""

"""thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)"""


set={"apple","banana","cherry"}
set.add("orange")
print(set)