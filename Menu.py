# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:06:22 2018

@author: n_zwan
Aaron Bolyard
Grace Rowse
"""

class Application:
    def __init__(self):
        self.students = None

def action_load_students_csv(app):
    app.students = file.readcsv(filename)

def action_list_all_students():
    for student in app.students:
        print(student)

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

def main():
  while True:
    action = getAction()

    print()
    action()
    print()

if __name__ == '__main__':
  main()
