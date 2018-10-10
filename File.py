# Aaron Bolyard, Grace Ross, Nick Zwan
# 2010-10-10
# Loads Students from a CSV.
# M3T

import csv
from arrays import Array
from Student import Student

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

if __name__ == "__main__":
	main()
