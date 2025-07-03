#you can use both double and single quotation in printing strings
print("double quotation")
print('single quotation')

print()

#if the content of the string has double quotation inside, you 
#should surround the whole string with single quotation vise-versa
print("My middle initial is 'A'")
print('My last name is "Albuero"')

#or just use backslash
print("My last name is \"Albuero\"")

print()

#for multiline string, use 3 double or single quotation
a = """Ako'y tutula
Mahabang-mahaba
Ako'y uupo
Tapos na po"""
print(a)

print()

#string is array, so you can call a certain position of a character or loop through it
b = "hello"
print(b[0], "is the letter in index 0") 

#looping
for x in b:
    print(x, end=" ") #use the end=" " to prevent line breaks and add space after each print

print() 
print()

#to know the number of characters inside a string, use the len() function
a = "four"
print(len(a))

print()

#check if a word is present in a string
statement = "Hi, my name is Dodong"
print("Dodong" in statement) #returns true
print("dodong" in statement) #returns false because it is case sensitive

#checks if not present in the string
print("Dingdong" not in statement) #returns true
print("name" not in statement) #returns false