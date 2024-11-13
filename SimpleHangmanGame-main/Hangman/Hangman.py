#---------------------------------IMPORT USER MODULES----------------------------------
import modules.common as common
import modules.game as game
import modules.game_rules as game_rules
import modules.game_hist as game_hist
import modules.game_stats as game_stats


#----------------------------------CREATE VARIABLES------------------------------------
choice=0
try_again='Y'
user_name=''
Try=''
word=''
Turns=0
TurnsUsed=0 
hintGiven=''
result=''

#------------------------------------CREATE LISTS-------------------------------------- 
#List of words

e_words=['cat','clock','doctor','driver','puppy','grapes','mouth',
         'soap','lipstick','garage','maths','broom','bark','nail',
         'ring','clip','root','goat','tap','park']

m_words=['butterfly','fence','hangar','ketchup','singer','kiwi',
         'moustache','kettle','grater','stethoscope','skateboard',
         'biology','sixty','ireland','backpack','fireworks','rocket',
         'yellow','peach','eleven']

h_words=['rhinoceros','technician','cheeseburger','croissant',
         'masseuse','intestine','saxophone','tambourine','wheelchair',
         'escalator','france','lymph','cryptography','hajj','quiz',
         'fizzy','absurd','jazz','cozy','jogging']

#List of hints

e_hint=['an animal','used to see the time','an occupation',
        'an occupation','an animal','a fruit','part of the face',
        'used to clean the body','a makeup item',
        'vehicles are parked here','subject','used to clean the house',
        'sound of an animal','used to hang something on the wall',
        'an accessory','an accessory','part of a tree','an animal',
        'get water from','place where kids play']


m_hint=['an insect','a guard for an outdoor area','place where aeroplanes are parked',
        'used as a relish','an occupation','a fruit','visible on the face',
        'found in the kitchen','found in the kitchen','used by doctors',
        'used to play','a subject','a number','a country','taken to school',
        'decorates the sky','a type of firework','a color','a fruit','a number']


h_hint=['an animal','an occupation','food','food','an occupation',
         'part of the human body','musical instrument','musical instrument',
         'used in the hospital','a staircase','a country',
         'a fluid containing white blood cells','a field of study','a festival/ritual',
         'a question-answer session','type of drink','illogical','a music genre',
         'comfort','exercise']



#------------------------------------PROCESS-------------------------------------------

#clear console
common.clearConsole()

#drops the perSession History table
game_hist.sessionTable()

#Welcomes the user
print ('\nWELCOME TO THE HANGMAN GAME!!\n') 
common.symbol()
print ('\n')

user_name = input ('Enter your name please: ').upper()

common.clearConsole()

print ("\nHi",user_name,"! \nHope you are doing good!!\n\nLET'S START\n")
print ("What would you like to do?\n")



#MENU SYSTEM

while try_again == 'Y' :
    
    #display the menu and get the choice
    choice=common.menu_choice()
    
    while True :
        Try = 'Y'
        
        #process for 1st choice
        if choice == 1 :

            #works when try is 'Y',i.e. if the user wants to replay the game
            while Try == 'Y' :

                common.symbol()

                #plays the game
                #gets the necessary varaiables from the respective functions
                date,Time = common.time_date()
                mode = game.game_mode()
                word = game.random_word(e_words,m_words,h_words)
                game.hide_word()
                Turns,TurnsUsed,hintGiven,result = game.find_word(e_hint,m_hint,h_hint)

                #Adds the data to the respective tables in the databases
                game_hist.datainput(date,Time,user_name,mode,word,Turns,TurnsUsed,hintGiven,result)
                game_hist.sessionData(date,Time,user_name,mode,word,Turns,TurnsUsed,hintGiven,result)

                #Asks the user if he/she needs to replay the game before going to the main menu
                while True:
                    Try = input('To play again, enter "Y": ').upper()
                    common.Exit(Try)
                    common.clearConsole()

                    #welcomes the user back if the user needs to play again
                    if Try == 'Y' :
                        print('\nHi again!!\n')
                        break
                    
                    #if the input is invalid or the user doesnt want to play again
                    else:
                        break
                    

        #process for 2nd choice    
        elif choice == 2 :
            common.symbol()

            #displays game rules
            game_rules.rules()
            

        #process for 3rd choice    
        elif choice == 3 :
            
            #works when try is 'Y',i.e. if the user wants to view other history
            while Try == 'Y' :

                common.symbol()

                #displays past game history
                game_hist.view_hist()

                #Asks the user if he/she needs to view other history
                while True:
                    Try = input('To view other history, enter "Y": ').upper()
                    common.Exit(Try)
                    common.clearConsole()

                    #welcomes the user back 
                    if Try == 'Y' :
                        print('\nHi again!!\n')
                        break
                    
                    #if the input is invalid or the user doesnt want to view again
                    else:
                        break
            

        #process for 4th choice    
        elif choice == 4 :
            #works when try is 'Y',i.e. if the user wants to view other stats
            while Try == 'Y' :

                common.symbol()

                #displays stats
                game_stats.html()

                #Asks the user if he/she needs to view other stats
                while True:
                    Try = input('To view other stats, enter "Y": ').upper()
                    common.Exit(Try)
                    common.clearConsole()

                    #welcomes the user back 
                    if Try == 'Y' :
                        print('\nHi again!!\n')
                        break
                    
                    #if the input is invalid or the user doesnt want to view again
                    else:
                        break
            
            

        #exits the program if choice is 99
        elif choice == 99 :
            exit()

        #process if the choice was invalid    
        else :
            print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
            break
        print()


        #process to try again
        while True : 
            try_again = input('To exit enter "N",To return to the main menu enter "Y": ').upper()
            common.Exit(try_again)
            common.clearConsole()

            #exits if the user enters 'N'
            if try_again == 'N':

                #clears the game history per session table
                game_hist.sessionTable()
                exit()

            #displays menu if the user enters 'Y'    
            elif try_again == 'Y' :
                choice=common.menu_choice()
                break

            #if the user input is invalid
            else :
                print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
            


