
# Division (/), Integer Division (//), Remainder (%), Exponent (**), Unary Negative (-), Unary Positive (+)

y = 5
x = 3
z = x % y

z = -z

print(f'result is {z}')

# Bitwise operator (& | ^ << >>)

x = 0x0a
y = 0x02
z = x << y

print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# Comparision Operators
x = 42
y = 73

if x < y:
    print('comparision is true')
else:
    print('comparision is false')

if x > y:
    print('comparision is true')
else:
    print('comparision is false')

if x != y:
    print('comparision is true')
else:
    print('comparision is false')

if x == y:
    print('comparision is true')
else:
    print('comparision is false')


# Boolean Operators
a = True
b = False
x = ('bear', 'bunny', 'tree')
y = 'tree'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if a or b:
    print('expression is true')
else:
    print('expression is false')

if not b:
    print('expression is true')
else:
    print('expression is false')

if y and x:
    print('expression is true')
else:
    print('expression is false')


if y is x[2]:
    print('expression is true')
else:
    print('expression is false')

print(id(y))
print(id(x[2]))

# Operator Precedence

print( 2 + 4 * 5) 
