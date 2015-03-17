continu = True
while continu == True:
    try: 
        number = int(input("Please enter a number between 1 and 100: "))
        if 1 <= number <= 100:
            print(number)
            continu = False
        elif number < 1 :
            print("number is too small")
        elif number > 100:
            print("number is too big")
    except ValueError:
        print("The value entered was not a number")     
