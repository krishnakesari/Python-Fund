# Sequence

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq] 
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


# Only divisible by 3
def main():
    seq = range(11)
    seq2 = [x for x in seq if x % 3 != 0] 
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


# Creating a list of tuples

def main():
    seq = range(11)
    seq2 = [(x, x ** 2) for x in seq] 
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


# Calling functions - rounding 'pi' with a sequence

def main():
    seq = range(11)
    from math import pi
    seq2 = [round(pi, i) for i in seq] 
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

# Create a dictionary

def main():
    seq = range(11)
    from math import pi
    seq2 = { x : x**2 for x in seq}   # Square
    print_list(seq)
    print(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()


# Everything not 'pd' in 'superduper'

def main():
    seq = range(11)
    from math import pi
    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq)
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()










