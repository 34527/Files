#Write a program that reads in 5 lines of text the user types in at the keyboard.
#As each line is typed in, the program should write the line to a text file.
#Euan McElhoney

with open("names.txt", mode="w", encoding = "utf-8") as Names:
    for count in range(5):
        Names.write(input("Please enter a name: "))
        Names.write("\n")

with open("names.txt", mode="r", encoding = "utf-8") as Names:
    print("You entered the names:")
    for line in Names:
        print(line, end = "")
    
