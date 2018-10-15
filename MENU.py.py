# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 13:33:01 2018

@author: n_zwa
"""

import file

class Application:
    def __init__(self):
        self.students = None

def action_grab_students_csv(app):
    app.students = file.readcsv(filename)

def action_list_students(app):
    for student in app.students:
        print(student)
    pass

    class Program:()
    def __init__(self):
        self.program = None

def action_get_program(app):
    pass

def action_quit(app):
    exit()
    
Actions = {
        'A': action_grab_students_csv,
        'B': action_list_students,
        'C': action_get_program,
        'Q': action_quit
}

def getAction():
    while True:
        print('A) Load Students from CSV.')
        print('B) List all Students.')
        print('C) Show students by program')
        print('Q) Quit.')
        
        choice = input