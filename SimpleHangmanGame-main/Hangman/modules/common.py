#---------------------------------IMPORT USER MODULES----------------------------------
import modules.common as common
import modules.game_hist as game_hist


#----------------------------------DEFINING FUNCTIONS----------------------------------
#--------------------------------------FUNCTION 1-------------------------------------- 

def menu() :
    '''This function will print the menu to the user'''
    
    print()
    common.symbol()
    print('1.  Play Hangman game',
          '\n2.  Rules to play hangman game',
          '\n3.  View the past game history',
          '\n4.  View Stats',
          '\n99. Exit',
          '\n\n\u25CFIF YOU WANT TO EXIT THE GAME AT ANY TIME, TYPE "EXIT"\n\n')


#--------------------------------------FUNCTION 2-------------------------------------- 

def menu_choice():
    '''
    This function will get the choice from the user

    Returns:
        choice: The number which is the choice chosen by the user from the menu

    '''
    
    while True:
        c = ''
        choice = 0
        
        try :
            #gets the choice from the user
            common.menu()
            c=input('Enter your choice: ')
            common.clearConsole()
            common.Exit(c)
            choice=int(c)
            break
        
        except ValueError :
            #if input is invalid raises an error
            print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
            continue
        
    return choice


#--------------------------------------FUNCTION 3-------------------------------------- 

def is_letter(value):
    '''
    This function will check if the user input is an alphabet

    Parameters:
        value: a string value which is checked if it is an alphabet

    Returns:
        bool(value in alpha): Contains a Boolean value True or False 
    '''
    
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F',
           'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z']
    return(bool(value in alpha))


#--------------------------------------FUNCTION 4-------------------------------------- 

def symbol():
    '''This function will print the hangman symbol'''
    
    print("""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  ---
                   """)


#--------------------------------------FUNCTION 5-------------------------------------- 

def Exit(val):
    '''
    This function will exit from the program

    Parameters:
        val: the string value to be checked if it is 'EXIT'

    '''
    #program will exit if val is 'EXIT'
    if val.upper()=='EXIT':
        game_hist.sessionTable()
        exit()


#--------------------------------------FUNCTION 6-------------------------------------- 

def time_date() :
    '''
    This function will get the current date and time

    Returns:
        date: This contains the current date
        Time: This contains the current time

    
    '''

    #importinng built-in modules
    import datetime
    import time

    #getting the current date and time according to the needed format
    date = datetime.date.today().strftime('%d %b %Y')
    Time = time.strftime('%H:%M')

    return date,Time


#--------------------------------------FUNCTION 7-------------------------------------- 

def clearConsole() :
    '''This function will clear the console'''

    #importing built-in modules
    import os

    #process to clear the console
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
          
        
