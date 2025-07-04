#Lists are ordered, changeable, and allows duplicate values

#use [] when declaring a list
animals = ["dog", "mouse", "cat", "mouse", "crocodile"] #duplicates are allowed

#to know how many items are there in the list, use len() function
print(len(animals), "items in the list") #outputs 4

#accesing the list
print(animals[0], "is the item in index 0")
print(animals[-1], "is the item in the last index") #use negative indexing to get the last item
print(animals[1:4], "are the items from index 1 to index 3") 
print(animals[:3], "are the items from start to index 2")
print(animals[2:], "are the items from index 2 to the last item")

print()

#changing the items in the list
things = ["mouse", "keyboard", "charger", "wheel", "towel"]
things[0] = "keychain" #changes the value of index 0 to "keychain"
print(things)

things[1:3] = ["fan", "wallet"] #changes the value of index 1 to index 2
print(things) 

things[1:3] = ["nailcutter"] #removes the value from index 1 to index 2 then repolace it with only 1 value(from 5 items to 4 items)
print(things) 

print()

#inserting a value to the list(added to the last)
things.insert(0, "coin") #first argument is at what index you want to insert and the second argument is the value
print(things)

#append a value(added to the end of the list)
things.append("battery") #added to the end of the list
print(things)

#extending a list(combining 2 lists)
partOne = [1, 2, 3]
partTwo = [4, 5, 6]

partOne.extend(partTwo) 
print(partOne)

print()

#removing items in the list
fruits = ["apple", "banana", "mango", "guava", "grapes", "pineapple", "dragon fruit", "orange"]
print(fruits)

#remove() removes the first occurence of the value you entered on the argument
fruits.remove("apple")
print(fruits, "apple is gone")

#pop() removes the item in a specified index and if you didn't specify the index, the last item will be removed
fruits.pop(3)
print(fruits, "grapes is gone because it is in index 3")

fruits.pop() #last item will be removed
print(fruits, "orange is gone because it is the last item")

#you can also use del keyword to delete an item
del fruits[1] #if you didn't specify the index, the entire variable will be deleted
print(fruits, "mango is gone because it is in the index 1")

#to clear all the values, use clear() function
fruits.clear()
print(fruits, "no items in the list because it was cleared")

print()

#sorting a list
numbers = [5, 7, 3, 1, 2, 6, 4]
numbers.sort()
print(numbers)

#reverse sorting(descending)
numbers.sort(reverse = True) #use reverse = True
print(numbers)

print()

#3 ways to copy a list
condiments = ["asukal", "asin", "paminta", "sa lunes babayaran"]

#method 1
condimentsCopy1 = condiments.copy()
print(condimentsCopy1)

#method 2
condimentsCopy2 = list(condiments)
print(condimentsCopy2)

#method 3
condimentsCopy3 = condiments[:]
print(condimentsCopy3)