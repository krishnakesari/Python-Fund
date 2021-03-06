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