# Type of the value
x = 7
print('x is {}'.format(x))
print(type(x))

#  String Type

x = 'seven'.upper()
print('x is {}'.format(x))
print(type(x))

## F -strings
a = 8
b = 9

x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))

### OR

x = 'seven {} {}'.format(8,9)
print('x is {}'.format(x))
print(type(x))

# Numeric Type
x = 7
print('x is {}'.format(x))
print(type(x))

y = 7 % 3 # Division 
print(y)

z = 7 // 3 # Reminder
print(z)

from decimal import *

a = Decimal('.10')
b = Decimal('.30')
x = a + a + a -b
print('x is {}'.format(x))
print(type(x))

# Boolean Type
x = True
print('x is {}'.format(x))
print(type(x))

if x:
    print("True")
else:
    print("False")


# Sequence Type
x = [1,2,3,4,5]
x[2]
for i in x :
    print('i is {}'.format(i))

x = [1,2,3,4,5]
x[0] = 45
for i in x :
    print('i is {}'.format(i))

x = range(5,10, 2) # (minimum, maximum and step)
for i in x :
    print('i is {}'.format(i))

x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5 }
for k, v in x.items():
    print('x is {}'.format(x))

