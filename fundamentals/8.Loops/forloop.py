#for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["banana", "apple", "orange", "pineapple", "guava"]

for i in fruits: #the i represents every item in a collection
    print(i) 

print()

#iterating through strings
word = "hello"

for i in word:
    print(i) # prints every letter in a string

print()

#break statement in for loop
for i in fruits:
    print(i)
    if i == "orange": #if the item is orange it stops the loop
        break

print()

#continue statement in for loop
for i in fruits:
    if i == "apple": #if the item is apple, it will skip the other code below then continue to the next iteration
        continue
    print(i)