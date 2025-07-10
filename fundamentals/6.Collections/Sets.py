#sets are unordered, unchangeable but can remove or add, unindexed, and doesn't allow duplicates

#to declare, use curly braces {}
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#to access, use iteration or looping
for x in numbers:
    print(x) 

print()

print(numbers)

#to add one item, use add() method
numbers.add(99)

#to add collections to a set, use update
tuples = (100, 200, 300)
lists = [400, 500, 600]
dictionaries = {
    "sevenh": 700,
    "eighth": 800,
    "nineh": 900
}

numbers.update(tuples) #adding a tuple 
print(numbers, " after adding the tuple")

numbers.update(lists) # adding a list
print(numbers, "after adding the list")

numbers.update(dictionaries.items()) #after adding the dictionary and i use items() method to show both pairs
print(numbers, "after adding the dictionary")

print()

#to remove an item, you can use both remove() or discard() methods
numbers.remove(99) #if the value does not exist, it will raise an error if you use remove() method
numbers.discard(100) #if  the value doesnt exist, it will not raise an error when using discard() method
print(numbers)

print()

#joining sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

unionResult = set1.union(set2) #joins 2 sets
print(unionResult)

intersectionResult = set1.intersection(set2) #keeps only the duplicate
print(intersectionResult)

differenceResult = set1.difference(set2) #keeps the items in set1 that are not in the set 2
print(differenceResult)

symmDifferenceResult = set1.symmetric_difference(set2) #keeps all items except the duplicate
print(symmDifferenceResult)
