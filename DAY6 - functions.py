def my_function():
  print("Hello from a function")

my_function()

#variable outside function
fname="khushi"
def my_name(fname):
  print(fname + " Refsnes")
my_name(fname)

#variable in function argument
def my_name(fname):
    print(fname + " Refsnes")
my_name("cynthia")

#variable in function parameter
def name(fname="emil"):
    print(fname + " Refsnes")
name()
name("cynthia")

#arbitrary functions
def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")

#keyword value args
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#return statements
def my_function(x):
  return 5 * x

(my_function(3))
print("yes")
print(my_function(5))
print(my_function(9))

#positional arguments
def number(x, /):
    print(x)
number(5)
#number(x=5) is not allowed being a keyword arg

#keyword arguments
def number2(*, x):
    print(x)
number2(x=10)

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
#the if statement runs until the condition k>0 holds true for given argument which here is 6
#it runs until it hits 0
"""tri_recursion(6)
 └→ tri_recursion(5)
     └→ tri_recursion(4)
         └→ tri_recursion(3)
             └→ tri_recursion(2)
                 └→ tri_recursion(1)
                     └→ tri_recursion(0) → returns 0
----------------------------
tri_recursion(1): 1 + 0 → 1 → print(1) → return 1
tri_recursion(2): 2 + 1 → 3 → print(3) → return 3
tri_recursion(3): 3 + 3 → 6 → print(6) → return 6
tri_recursion(4): 4 + 6 →10 → print(10) → return10
tri_recursion(5): 5 +10 →15 → print(15) → return15
tri_recursion(6): 6 +15 →21 → print(21) → return21
-----------------------------
#simpler explanation
You put block 1 → you have 1 block → you say 1.

You put block 2 → now you have 1 + 2 = 3 blocks → you say 3.

You put block 3 → 3 + 3 = 6 → you say 6.

You put block 4 → 6 + 4 = 10 → you say 10.

You put block 5 → 10 + 5 = 15 → you say 15.

You put block 6 → 15 + 6 = 21 → you say 21.
"""