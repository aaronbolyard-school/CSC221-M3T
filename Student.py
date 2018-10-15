"""
Authors: Grace Ross, Aaron Bolyard, Nick Zwan 
"""

def getProgram(program):
    '''Dictionary holds names of programs'''
    PROGRAMS = {
        "A25590S": "Systems Security and Analysis",
        "A25590C": "Computer Programming and Development",
        "A25590N": "Network Management",
        }
    
    return PROGRAMS.get(program,program)

class Student:
    '''Created the Student class to hold student information'''
    def __init__(self, row):
        self.ID = (row[0])
        self.firstName = row[1]
        self.lastName = row[2]
        self.program = row[3]
        self.startDate = row[4]
        self.advLastName = row[5]
        self.mostRecentTerm = row[6]
        self.gpa = float(row[7])

    '''Prints the student info in a readable format'''   
    def __str__(self):
        return str.ljust(self.ID, 10) + " " + str.ljust(self.firstName, 15) + " " + str.ljust(self.lastName, 20) + " " + str.ljust(getProgram(self.program), 25)

        
        
    
