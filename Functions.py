# Basic unit of re usable code

def main():
    kitten(5) # Code block

def kitten(n):
    print(f'{n} Meow.')

if __name__ == '__main__':main()  # Very commonly used to build modules


# Function Arguments


def main():
    kitten(5,6,7) # Code block

def kitten(a, b, c):
    print('Meow.')
    print(a, b, c)

if __name__ == '__main__':main()  # Very commonly used to build modules


# Call by value, 
def main():
    x = 5
    print(id(x))
    kitten(x) # Code block
    print(f'in main: x is {x}')

def kitten(a):
    print(id(a))
    a = 3
    print(id(a))
    print('Meow.')
    print(a)

if __name__ == '__main__':main()  # Very commonly used to build modules

# Call by reference,

def main():
    x = [5] # One element list
    kitten(x) # Code block
    print(f'in main: x is {x}')

def kitten(a):
    a[0] = 3 # call by reference - changing an element in the list
    print('Meow.')
    print(a)

if __name__ == '__main__':main()  # Very commonly used to build modules

# Variable length argument list: 

def main():
    kitten('meow', 'grrr', 'purr') # tuple

def kitten(*args):   # variable length argument list
    if len(args):
        for s in args:
            print(s)
    else:
        print('Meow.')

if __name__ == '__main__': main()

# Keyword Arguments

def main():
    kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'purr') # Dictionary 

def kitten(**kwargs):  #(two astrix to pass dictionary)
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Meow.')

if __name__ == '__main__' : main()

# Return Values:

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    return [42, 43, 44]  # return list

if __name__ == '__main__': main()


def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    return dict(x = 42, y = 43, z = 44) # return dictionary

if __name__ == '__main__': main()


# Generator - results a series of values 

def main():
    for i in inclusive_range(5, 25, 4):  # (start, stop, step)
        print(i, end = ' ')
    print()

def inclusive_range(*args): # variable argument list
    numargs = len(args)
    start = 0
    step = 1

    # Initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop  = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    ## generator
    i = start
    while i <= stop:
        yield i             # same as return for generators
        i += step
    
if __name__ == '__main__': main()


# Decorator - returns a wrapper function

def f1():
    print('this is f1')

x = f1
x()



def f1():
    def f2():
        print('this is f2')
    return f2
x = f1()
x()


import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2-t1) * 1000} ms')
    return wrapper

@elapsed_time  # decorator

def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()





























