"""
Authors: Grace Ross, Aaron Bolyard, & Nick Zwan
M3T - Draft
"""
import csv
from arrays import Array
from Student import Student

def action_load_student_csv():
    pass

def action_list_all_students():
    pass

def action_list_programs():
    pass

def action_quit():
    exit()

ACTIONS = {
    'A': action_load_student_csv,
    'B': action_list_all_students,
    'C': action_list_programs,
    'Q': action_quit
    }

def getAction():
    while True:
        print("A) Load Students from CSV")
        print("B) List All Students")
        print("C) List Students by Program")
        print("Q) Quit")

        userInput = input("Enter action: ").upper()
        action = ACTIONS.get(userInput, None)

        if action == None:
            print("Please enter a valid option.")
        else:
            return action

def countLinesInFile(filename):
    """
    Counts lines in 'filename'. 	
    Returns the count.
    """

    with open(filename, 'r') as file:
        numLines = 0
        for line in file:
            print(line)
            numLines += 1

    return numLines

def readCSV(filename):
    """
    Reads the CSV from 'filename' and returns a Student array.
    The first line of the CSV is expected to be a header with column names.
    Returns the Array of Students.
    """

    numLines = countLinesInFile(filename)

    # The first line is the header.
    students = Array(numLines - 1)

    with open(filename, 'r') as file:
        reader = csv.reader(file)

	# Skip header.
        for row in reader:
            break

        currentIndex = 0
        for row in reader:
            students[currentIndex] = Student(row)
            currentIndex += 1

        assert(currentIndex == len(students))

    return students

def main():
    students = readCSV("student_advisees_testdata.csv")

    for student in students:
        print(student)

    while True:
        action = getAction()

        print()
        action()
        print()
        
if __name__ == '__main__':
  main()

