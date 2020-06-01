print('Hello, World.')

print('Something entirely different')

## Expressions and statements

import platform
print('This is python version {}'.format(platform.python_version()))


## Hello Main - Define functions before they are called 

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

if __name__ == '__main__': main()


## Expressions - literals, identifiers, values, function calls and operations
## Statement is a line of code

