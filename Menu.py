# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:06:22 2018

@author: n_zwan
Aaron Bolyard
Grace Rowse
"""
def main():
   search = input('Do you want to perform a data search? Y or N?')
    #gpaSearch = input('Do you want to display by student GPA? Y or N') 
    #programSearch = input('Do you want to display by start date?')
   start = input('Press A + enter to search by name or B + enter to search by Last name')
    
   if search == 'Y':
       start()
   elif search == 'N':
       print('Goodbye')
   else:
       print('Please enter a valid option')

   if start =='A':
       print('x')
   if start == 'B':
        print('y')
   else:
       print('Please enter a valid option')

main()
        
   
    
        
    

            
            
        
        
