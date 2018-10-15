# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:06:22 2018

Nick Zwan
Aaron Bolyard
Grace Rowse
"""

import File
""" 
Creates a class called Application.
"""

class Application:
  def __init__(self):
    self.students = None
"""
Loads file from user input. 
if incorrect prints exception.
"""
def action_load_student_csv(app):
  try:
    filename = input("Enter a filename: ")
    app.students = File.readCSV(filename)
  except Exception as e:
    print("Couldn't load students:", e)

"""
Loads students csv file and prints student info.
"""
def action_list_all_students(app):
  if not app.students:
    print("Please load the students CSV first.")
  else:
    for student in app.students:
      print(student)

"""
Generates program list.
"""
def action_list_programs(app):
  pass

"""
Allows user to exit program.
"""
def action_quit(app):
  exit()

"""
Creates a dictionary to generate menu that accepts user input. 
"""
ACTIONS = {
  'A': action_load_student_csv,
  'B': action_list_all_students,
  'C': action_list_programs,
  'Q': action_quit
}

"""
Presents a menu for user. 
If input incorrect program returns
an exception.
"""
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

"""
Returns Data based on user input.
"""
def main():
  app = Application()

  while True:
    action = getAction()

    print()
    action(app)
    print()


if __name__ == '__main__':
  main()
