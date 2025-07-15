#dictionaries are ordered, changeable, and doesnt allow duplicates(for key names only)
#very similar to json

#declaring a dictionary
person = {
    "name": "Cedrick",
    "age": 20,
    "sex": "male"
}

#accessing the value (use the keys)
print(person["name"])
print(person.get("name")) #you can also use this

print()

#getting the keys in the dict
print(person.keys())

#changing values of dict
person["age"] = 21
print(person)

#adding values (almost the same as updating)
person["hobbies"] = "playing online games"
print(person)

#removing values
person.pop("age") #removes a specific item
print(person)
person.popitem() #removes the last item
print(person)

#copying dictionary
dictOne = {
    "color": "blue",
    "quantity": 23
}

dictTwo = dictOne.copy() #use copy() function to copy the dictionary