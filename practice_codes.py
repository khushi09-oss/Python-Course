"""# taking user input
a = input("First number: ")
b = input("Second number: ")

# converting input to float and adding
res1 = float(a) + float(b)
res2 = int(a) + int(b)


print(res1)
print(res2)"""

# function to add two numbers
"""def add(a, b):
    return a + b

# initializing numbers
a = 10
b = 5

# calling function
res = add(a,b)

print(res)"""

#function without return and global variable
"""def add2(a, b):
    print(a+b)

add2(10,5)"""

"""import operator
print(operator.add(10,5))

print(10+5)
print(sum([10,5]))"""

a=7
b=10
"""print("max value is:", max(a,b))

print("max value is : ",a if a > b else b)

if a > b:
    print(a)
else:
    print(b)"""

"""num = [a, b]
num.sort()
print(num[-1])"""


"""n = 6
# Initialize the factorial variable to 1
fact = 1
# Calculate the factorial using a for loop
for i in range(1, n + 1):
    fact *= i #fact * i = 1 * i
    #6x5x4x3x2x1
print(fact)"""


"""def fact(n):
    # single line to find factorial
    return 1 if (n == 1 or n == 0) else n * fact(n -1)


# Driver Code
num = 5
print(fact(num))

import numpy
n=5
x=numpy.prod([i for i in range(1,n+1)])
print(x)"""

# Python3 program to find compound
# interest for input taking from user.


def compound_interest(principal, rate, time):

    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)


# Driver Code
#Taking input from user.
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))
#Function Call
compound_interest(principal,rate,time)

#This code is contributed by Vinay Pinjala.

