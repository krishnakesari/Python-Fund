

def main():
    a = set("I am fine")
    b = set("I am ok")
    print_set(sorted(a))
    print_set(sorted(b))

def print_set(o):
    print('{', end = ' ')
    for x in o: print(x, end = ' ')
    print('}')

if __name__ == '__main__': main()


# Members in set a but not b
def main():
    a = set("I am fine")
    b = set("I am ok")
    print_set(a - b) # Members are in a but not b

def print_set(o):
    print('Members with a but not b{', end = ' ')
    for x in o: print(x, end = ' ')
    print('}')

if __name__ == '__main__': main()

# Members in set a or b  or both

def main():
    a = set("I am fine")
    b = set("I am ok")
    print_set(a | b)

def print_set(o):
    print('Members with a or b or both:  {', end = ' ')
    for x in o: print(x, end = ' ')
    print('}')

if __name__ == '__main__': main()


# Members in set a or b  not both

def main():
    a = set("I am fine")
    b = set("I am ok")
    print_set(a ^ b)

def print_set(o):
    print('Members with a or b but not both:  {', end = ' ')
    for x in o: print(x, end = ' ')
    print('}')

if __name__ == '__main__': main()

# Members in both set a and b

def main():
    a = set("I am fine")
    b = set("I am ok")
    print_set(a & b)

def print_set(o):
    print('Members with both a and b are:  {', end = ' ')
    for x in o: print(x, end = ' ')
    print('}')

if __name__ == '__main__': main()

