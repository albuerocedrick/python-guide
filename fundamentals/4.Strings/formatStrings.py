#string interppolation or what we called F-string or Format string in python

firstName = "Cedrick"
lastName = "Albuero"
age = 20

#instead of concatenation like this
print("Hi, my name is " + firstName + " " + lastName + " and I'm " + str(age) + " years old") #this is too long
#or
print("Hi, my name is", firstName, lastName, "and I'm", age, "years old")

#we will use F-string to make it easier
#just add f before the double or single quotation
#and if adding a variable, use a curly bracket{}
print(f"Hi, my name is {firstName} {lastName} and I'm {age} years old")

#you can also use f-string to limit  the decimal places of a number
number = 4.33333333
print(f"{number:.2f}") #by 2 decimal places
print(f"{number:.3f}") #by 3 decimal places