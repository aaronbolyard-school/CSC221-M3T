# -*- coding: utf-8 -*-
"""
Author: Grace Ross, Aaron Bolyard, Nick Zwan
This program 
"""

class Student:
    def __init__(self, row):
        self.ID = (row[0])
        self.firstName = row[1]
        self.lastName = row[2]
        self.program = row[3]
        self.startDate = row[4]
        self.advLastName = row[5]
        self.mostRecentTerm = row[6]
        self.gpa = float(row[7])
       