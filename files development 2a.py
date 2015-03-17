#Euan McElhoney
#Files - Development 2a

#Write a program that reads a name and date of birth typed
#in at the keyboard and saves it as a list to a binary file.

import pickle

class Info:
    def __init__(self):
        self.name = None
        self.dob = None


people = []

record = Info()
record.name = input("Please enter a name: ")
record.dob = input("Please enter their date of birth: ")
people.append(record)


with open("info.dat", mode = "wb") as people_info:
    pickle.dump(people, people_info)
    
