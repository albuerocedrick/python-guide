#type conversion is called "casting" in python

#string to integer
a = "5" #a string
print(a, "is a string and i can't perform an arithmetic operation")
b = int(a) #i will convert it to an int
print(b, "is an integer and i can perform an arithmetic operation now")

print()

#float to int (mawawala ang decimal)
c = 3.99 #float data type
print(c, "is a float")
d = int(c) #converts to int
print(d, "is an integer now, i lost my decimal value")

print()

#int to float
e = 50
print(e, "is an integer, i don't have decimal value")
f = float(e)
print(f, "is now a float, i have decimal value")