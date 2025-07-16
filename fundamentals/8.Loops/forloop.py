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

print()

#using range() in for loop
for i in range(6): #this will loop starting from 0-6
    print(i)

print()

#if you want to start at a specific number, you can specify it like this range(starting point, end point)
for i in range(3, 6): #will loop from 3-5
    print(i) 

print()

#the default increment of for loop is 1 but you can also specify it by adding another parameter
#like this range (starting point, end point, increment value)
for i in range(1, 31, 2): #this will increment by 2
    print(i)

print()

#using else keyword in for loop
#else keyword will not run if it is stopped by a break statement
for i in range(6):
    print(i)
else:
    print("loop is done!")

print()

#nested for loop
firstname = ["malaking", "maliit na", "masarap na"]
lastname = ["mansanas", "saging", "bayabas"]

for i in firstname:
    for x in lastname:
        print(i, x)
