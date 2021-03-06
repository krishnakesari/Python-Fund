 
# List - sequence - mutable -[]
# Tuple - immutable - ()
# Dictionary - array or hashed array - {}
# set - set of values - {}

## Lists
def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[1:3:2]) # defining index parameters start, end, step
    i = game.index('Paper') # defining index by list value
    print(game[i])
    game.insert(0, 'Computer') # Adding a value to list
    game.remove('Spock') # remove a value
    del game[3] # remove a value using index
    print(', '.join(game)) # Join a value ',' comma to each value
    print(len(game)) # print length of list
    game.pop() # Removes an item from the end of the list
    print_list(game)

def print_list(o):
    for i in o : print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()


## Tuple works just like list but it is immutable
# def main():
#     game = ('computer', 'mobile')
#     game.append('watch')
#     print_list(game)

# def print_list(o):
#     for i in o: print(i, end=' ', flush=True)
#     print()

# if __name__ == '__main__': main()

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










