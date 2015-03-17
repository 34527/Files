#Euan McElhoney
#Files - Development 2b

import pickle

class Info:
    def __init__(self):
        self.name = None
        self.dob = None

with open("info.dat", mode = "rb") as people_info:
    pickle.load(people_info)

for person in people:
    print(record.name)
    print(record.dob)
    
    
