#match is the same as the switch statement
#same as the if...else statement but for equal values only
day = 1

match day:
    case 1: #if the value is equals to 1
        print("monday")
    case 2: 
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5: 
        print("Friday")
    case _: #use this as an else
        print("invalid value")

#combining values
match day:
    case 1 | 2 | 3 | 4 | 5: #use | to check more than 1 value match
        print('weekdays')
    case 6 | 7:
        print('weekend')
    case _:
        print("invalid number")

#you can also use if statement in a case statement
weather = "rainy"

match day:
    case 1 | 2 | 3 | 4 | 5 if weather == "rainy":
        print("rainy on weekdays")
    case 1 | 2 | 3 | 4 | 5 if weather == "sunny":
        print("sunny on weekdays")
    case _:
        print("invalid number")