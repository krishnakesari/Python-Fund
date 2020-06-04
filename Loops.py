# While loop - body is true, expresses condition 
# For loop is an iterator - executes each item in the sequence

# While loop should have a statement that will result in true to close the loop
secret = "swordfish"
pw = ''

while pw != secret:
    pw = input("what's the secret word ? ")


# Continue (Testing condition again), else (only if the loop ends normally) and break (stopping loop prematurely)
secret = "swordfish"
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt: break
    if count == 3: continue
    pw = input(f"{count}: what's the secret word ? ")

else:
    auth = True
print("Authorized" if auth else "Calling the FBI ...")


# For loop

animals = ('bear', 'bunny', 'dog', 'cat')

for pet in animals:
    if pet == 'dog':continue
   # if pet == 'cat': break
    print(pet)
else:
    print('that is all of the animals')



