#Exceptions continued
try:
 x = 7/0
 print(x)
except:
    print("number cannot be divided by zero")

#multiple except blocks
try:

    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound

# program to print the reciprocal of even numbers

#try...else
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

#try finally


