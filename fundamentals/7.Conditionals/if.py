#in other langauge, they use curly braces to  contain a clock of code
#but in python the only thing you need is indentation
#for example:
#if(a > b) {
#     print("a is greater than b");
# }
#but in python:

a = 5
b = 4

#if statement
if a > b: # no need for parenthesis but colon is needed
    print("a is greater than b") #just indent the statement to inform the compiler that this block of code belongs to the if statement

#you can use this shorthand for single line
if a > b: print("a is greater than b")

print()

#if else statement
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

#shorthand for else if statement
print("a is greater than b") if a > b else print("b is greater than a")

print()

#if-elif-else statement
if a == 5:
    print("a is equal to 5")
elif a < 5:
    print("a is less than 5")
else:
    print("a is not equal and not less than 5")

#shorthand for if-elif-else statement
print("a is equal to 5") if a == 5 else print("a is less than 5") if a < 5 else print("a is not equal and not less than 5")

print()

#using "and" keyword (true if both contidions are true)
if a > b and a == 5:
    print('that is true') #will execute because both conditions are true

#using "or" keyword (true if atleast 1 condition is true)
if a > b and a != 5:
    print('that is true')  #the first condition is true but the other one is false, however, we only need 1 condition in "or" keyword to be true

#using "not" keyword to reverse the result
if not b > 5:
    print("b is not greater than 5")

#nested if-else
age = 19
sex = 'm'

if age >= 18: #if age is greater than or equals to 18
    #if true, this if-elif-else statement will execute
    if sex.upper() == 'M': #converts the string to upper case then checks if the condition is true
        print("He is legal age")
    elif sex.upper() == 'F':
        print("She is legal age")
    else:
        print("invalid sex") 
elif age < 18 and not age <= 0: #if age is less than 18 and age is not less than or equals to 0
    if sex.upper() == 'M':
        print("He is not legal age")
    elif sex.upper() == 'F':
        print("She is not legal age")
    else:
        print("invalid sex")
else:
    print("invalid age")

#if statements cannot be empty, so you need to put pass statement to avoid error
if a < 5: #this statement is false. since i don,t have an else statement, i will put the pass keyword 
    pass