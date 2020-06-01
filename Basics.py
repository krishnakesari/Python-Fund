print('Hello, World.')

print('Something entirely different')

## Expressions and statements

import platform
print('This is python version {}'.format(platform.python_version()))


## Hello Main - Define functions before they are called 

def main():
    message()  # Indented function adds white space 

def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()


## Expressions - literals, identifiers, values, function calls and operations
## Statement is a line of code

## White spaces - Indented function

## Print function evolution 
x = 42
print('x = %d' % x) # Used in Python 2
print('x = {}'.format(x)) # Used in Python 3 (Recommended to use)
print(f'x = {x}') # From Python 3.6 onwards

## Blocks and spaces
x = 42
y = 73
### Conditional Statement
if x < y: 
    print('x < y: x is {} and y is {}'. format(x, y))
else:
    print('something else')

