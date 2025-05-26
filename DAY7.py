#lambda function

"""def function_name(x):
    add=x+10
    print(add)

function_name(5)"""

x = lambda a: a + 10
print(x(5))

#exceptions
#zero division error
"""print(0 / 0)
number = 10

#self raised exception
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)"""

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux systems.")
    print("Doing Linux things.")

"""try:
    linux_interaction()
except RuntimeError as e:
    print(e)
    print("Something went wrong.")"""
graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
 }
print(graph)

from collections import deque
deque(['a','b','c'])
print(deque(['a','b','c']))
deque('abc')
print(deque('abc'))
deque([{'data': 'a'}, {'data': 'b'}])
print(deque([{'data': 'a'}, {'data': 'b'}]))

llist = deque("abcde")
print(llist)


llist.append("f")
print(llist)


print(llist.pop())


print(llist)









