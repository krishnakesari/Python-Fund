## Dictionary type
def main():
    animals = dict(Kitten = 'meow', puppy = 'ruff!')
   # animals = {'Kitten': 'meow', 'puppy': 'ruff!'} # Key-value pair
    for k, v in animals.items():
       print(f'{k}: {v}')
    # print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

######

# Only Keys 

def main():
    animals = dict(Kitten = 'meow', puppy = 'ruff!')
   # animals = {'Kitten': 'meow', 'puppy': 'ruff!'} # Key-value pair
    for k in animals.keys(): print(k)
    # print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

# Only values

def main():
    animals = dict(Kitten = 'meow', puppy = 'ruff!')
   # animals = {'Kitten': 'meow', 'puppy': 'ruff!'} # Key-value pair
    for v in animals.values(): print(v)
    # print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

# Subsets

def main():
    animals = dict(Kitten = 'meow', puppy = 'ruff!')
   # animals = {'Kitten': 'meow', 'puppy': 'ruff!'} # Key-value pair
    print(animals['puppy'])
    # print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

# Update a key / value:

def main():
    animals = dict(Kitten = 'meow', puppy = 'ruff!')
   # animals = {'Kitten': 'meow', 'puppy': 'ruff!'} # Key-value pair
    animals['puppy'] = 'I am a dog'
    print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()

# Validation of value

def main():
    animals = dict(Kitten = 'meow', puppy = 'ruff!')
   # animals = {'Kitten': 'meow', 'puppy': 'ruff!'} # Key-value pair
    print('found!' if 'dinosaur' in animals else 'nope!')
    print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
