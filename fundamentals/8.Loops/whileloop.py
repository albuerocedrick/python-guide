#while loop

number = 1

while number < 11: #it will loop until this is statement becomes false (will stop if the value becomes 11)
    print(number) #prints 1-10
    number += 1 #increment to avoid infinite loop

print()
number = 1

#using break statement in while loop
while number < 11:
    print(number)
    if number == 6:
        break #the loop will exit if the number becomes 6
    number += 1

print()
number = 0

#using continue statement in while loop
while number < 10:
    number += 1
    if number == 6: #if the number is equal to 6, it will skip
        continue;
    print(number)

#you can also use else statement when the condition is not true anymore to show that the loop has ended
number = 1

while number < 11:
    print(number)
    number += 1
else:
    print("the loop has ended")