#simple variable declaration and printing(no need semicolon)
name = "cedrick"
print(name)

print()

#assigning values to multiple variables
fname, lname, age = "cedrick", "albuero", 20
print(fname)
print(lname)
print(age)

print()

#assigning single value to multiple variables
a = b = c = "same lang kami"
print(a)
print(b)
print(c)

print()

#unpacking from a list(same as destructuring in javascript)
numbers = [1, 2, 3]
one, two, three = numbers
print(one)
print(two)
print(three)

print()

#in python contatenation, you cannot concatenate two different data types
#if you use plus sign(+). to make it happen, you should use comma(,)
#if you use comma for concatenation, it has a space between variables
#and if you use plus sign, no space between variables
number = 23
string = "not a number"
print(number, string) #meron agad space
#print(number + string) will show TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(str(number) + string) #alternative way if you really want to use plu sign

print()
