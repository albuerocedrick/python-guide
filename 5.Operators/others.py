#identity operators

#"is" keyword returns true if the vairables are the same
a = 5
b = 5
c = 3

print(a is b) #returns true
print(a is c) # returns false

#"is not" keyword returns true if variables are not the same
print(a is not c) # returns true
print(a is not b) #returns false


#membership operators
a = "I am a programmer"

#"in" keyword returns true if a specified value is present in the variable
print("programmer" in a) #returns true
print("sugar" in a) #returns false

#"not in" keyword returns true if not present
print("salt" not in a) #returns true
print("I am" not in a) #returns false
