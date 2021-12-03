from os import system, name
from packages import backup_check as bcheck
from packages import backup_wizard as bwizard
from time import sleep
import sys
import os
import posixpath


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def showing_text(text_document):
    textObject = open(text_document, "r")
    data = textObject.read()
    print(data)
    print("\n")

while True:
    os.system("cls")
    
    text_object = "ascii_image_small.txt"
    logoObject = showing_text(text_object)
    string01 = "Welcome to Backup assistant. Please choose an option:"
    print(string01)
    print("="*len(string01))
    print("1.- Start a backup")
    print("2.- Check a backup")
    print("3.- Documentation")
    print("4.- Exit\n")
    
    option = input()
    
    if option == "1":
        os.system("cls")
        user_name = input("What is your user name?\n")
        user_name = user_name.lower()
        unit = input("What is your storage device?\n")
        unit = unit.upper()
        print("="*10)
        
        while os.path.isdir(f"{unit}:\\") != True:
            print("The directory does not exist. Try again.")
            unit = input("What is your storage device?\n")
            unit = unit.upper()
        
        o_exit = True
        while o_exit == True:
            bwizard.backup_wizard(unit, user_name)
            print("="*10)
            request = input("Press any key to exit.\n")
            res = isinstance(request, str)
            if res == True:
                o_exit = False
        
        
    elif option == "2":
        os.system("cls")
        unit = input("What is your storage device?\n")
        unit = unit.upper()
        print("="*10)
        
        while os.path.isdir(f"{unit}:\\") != True:
            print("The directory does not exist. Try again.")
            unit = input("What is your storage device?\n")
            unit = unit.upper()

        o_exit = True
        while o_exit == True:
            bcheck.backup_date(unit)
            print("="*10)
            request = input("Press any key to exit.\n")
            res = isinstance(request, str)
            if res == True:
                o_exit = False
        
        
    elif option == "3":
        os.system("cls")
        o_exit = True
        text_doc = "\\backup_documentation.txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        full_path = dir_path + text_doc
        full_path.replace(os.sep, posixpath.sep)
        with open(full_path) as file:
            print(file.read())
        while o_exit == True:
            answer = input("Do you want to return to Menu? (y\\n)\n")
            answer = answer.lower()
            if answer == "y":
                o_exit = False
            else:
                print("Your option is invalid. Try again")
                sleep(2)
            
    elif option == "4":
        sys.exit()
        
    else:
        print("Your option is invalid. Try again")
        sleep(2)
        clear()