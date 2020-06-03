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

# Conditional Statement
x = 42
y = 73

if x < y: 
    print('x < y: x is {} and y is {}'. format(x, y))
elif x > y:
    print('x > y: x is {} and y is {}'. format(x, y))
elif x == y:
    print('x = y: x is {} and y is {}'. format(x, y))
else:
    print('something else')


# Loops 
## While loop
words = ['one', 'two', 'three', 'four', 'five']

n = 0
while (n < 5):
    print(words[n])
    n += 1

a, b = 0,1
while b < 1000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b 

## For loop - Sequence (conveniently simple)
for i in words:
    print(i)

# Functions
def function (n):
    print(n)
    return n * 2

x = function(47)
print(x)

## Is Prime or Not Prime function 
def isprime(n):
    if n <= 1:
        return False
    for x in range (2, n):
        if n % x == 0:
            return False
    else:
        return True

n = 6

if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} if not prime')

def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ', flush=True)

list_primes()

# Objects is an instance of a class (class is a definition)
class Duck:
    sound = 'Quakkkk!'
    walking = 'Walks like a duck.'

    def quack(self):
        print(self.sound)
    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()

