#tuple is ordered but not changable and allows duplicate

#to declare a tuple use parenthesis ()
colors = ("blue", "black", "green", "yellow")

#to determine the length, use len() method just like lists
print(len(colors), 'items inside the array')

print()

#if declaring a tuple with only one item inside, you should add comma to the end
gadgets = ("laptop",)  
animals = ("dog")

print("this is a", type(gadgets)) #tuple
print("this is a", type(animals)) #not a tuple

print()

#use index to access tuples
print(colors[0]) #first item
print(colors[-1]) #last item

print()

#to update and delete an item in tuple, convert it to list first then convert it back to tuple after modofying
numbers = (1, 2, 3, 4, 5, 6, 7 , 8, 9)
numbersList  = list(numbers) #convert using list constructor

numbersList[0] = 55 #modify the first item(index 0) in the list
numbersList.pop(3) #removing the 4th item(index 3) in the list

numbers = tuple(numbersList) #converting it back to tuple

print(numbers, "result after the modification")

print()

#to add items in  a tuple, the easiest way is to create another tuple and add it together
vehicles = ("car", "truck", "van", "tricycle")
addedVehicle = ("ebike",) #create another tuple to add, don't forget the comma if only 1 item

vehicles += addedVehicle # add them together
print(vehicles)

print()

#unpacking tuple values
a, b, c, d, e = vehicles
print(a)
print(b)
print(c)
print(d)
print(e)

#id the variables are fewer than the values use * to assign the excess items to a particular variable as a list
x, y, *z = vehicles
print(x) # "car"
print(y) # "truck"
print(z) # "van", "tricycle", "ebike"

#if you put the asterisk in the middle
x, *y, z = vehicles
print(x) # "car"
print(y) # "truck", "van", "tricycle"
print(z) # "ebike"



