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
def recursion(x):
    if (x>0):
        result = x + recursion(x - 1)
        print(result)
    else:
        result=0
        return result
recursion(3)