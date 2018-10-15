# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:06:22 2018

@author: n_zwan
Aaron Bolyard
Grace Ross
"""

import File

class Application:
  def __init__(self):
    self.students = None

def action_load_student_csv(app):
  try:
    filename = input("Enter a filename: ")
    app.students = File.readCSV(filename)
  except Exception as e:
    print("Couldn't load students:", e)

def action_list_all_students(app):
  if not app.students:
    print("Please load the students CSV first.")
  else:
    for student in app.students:
      print(student)

def action_list_programs(app):
  if not app.students:
    print("Please load the students CSV first.")
  else:
    programCode = input("Enter program code: ").upper()
    for student in app.students:
      if student.program == programCode:
        print(student)

def action_quit(app):
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
  app = Application()

  while True:
    action = getAction()

    print()
    action(app)
    print()

if __name__ == '__main__':
  main()
