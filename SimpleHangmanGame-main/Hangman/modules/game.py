#---------------------------------IMPORT MODULES----------------------------------
#user modules
import modules.common as common

#built-in modules
import random

#Assigning variables
mode=''
word=''
hidden_word=''
hint=''
rand=0
hintGiven=''

#Creating lists
Index=[]
hidden_word_list=[]
guessed=[]



#----------------------------------DEFINING FUNCTIONS----------------------------------
#--------------------------------------FUNCTION 1-------------------------------------- 
def game_mode():
    '''
    This function will get the game mode the user wishes to play

    returns:
        Mode : Mode is a string value which contains the game mode chosen by the user

    '''

    #Defining global variables
    global mode

    #Assigning it an empty string
    mode=''

    #Getting the mode from the user
    while mode == '' :
        print ('\nWhich mode would you like to play?')
        mode = input('Enter "E" for easy, "M" for medium and "H" for hard mode: ').upper()
        
        common.clearConsole()
        common.Exit(mode)
        
        if mode == 'E' or mode == 'M' or mode == 'H':
            if mode== 'E' :
                Mode = 'EASY'
            elif mode == 'M' :
                Mode = 'MEDIUM'
            elif mode == 'H' :
                Mode = 'HARD'
        else:
            mode = ''
            print ('\n\nInvalid input! Please try again\n')
    return Mode

    
#--------------------------------------FUNCTION 2--------------------------------------

def random_word(word_1,word_2,word_3):
    '''
    This function will get a random word from the lists according to the game mode

    Parameters:
        word_1: A list of words
        word_2: A list of words
        word_3: A list of words

    Returns:
        word: The string value which contains the random word
    '''

    #Defining global variables
    global mode,word,hidden_word,rand

    #getting a random number from 0-20
    rand=random.randrange(0,20)

    #getting the random word from the respective list
    if mode == 'E':
        word = word_1[rand].upper()
    if mode == 'M':
        word = word_2[rand].upper()
    if mode == 'H':
        word = word_3[rand].upper()

        
    return word

    
#--------------------------------------FUNCTION 3--------------------------------------

def hide_word():
    '''This function will hide the word with underscores'''

    #Defining global variables
    global hidden_word_list,word

    #Creating an empty list
    hidden_word_list=[]

    #Replaces the letter with underscores
    for i in range(len(word)):
        
        #checks if the character is space
        if ord(word[i]) == 32:
            hidden_word_list.append(' ')
            
        else:
            hidden_word_list.append('_')
    

#--------------------------------------FUNCTION 4--------------------------------------

def find_index(word,guess):
    '''
    This function will find the index of guess in word

    Parameters:
        word: The string value in which the index of guess should be found
        guess: The string value to get the index of

    Returns:
        Index: A list which contains the index/indexes of guess in word
    '''

    #Defining global variables
    global Index

    #Creating an empty list
    Index = []

    #Getting the index of guess
    for i in range(len(word)):
        
        if guess == word[i] :
            
            #Appending the index to the list
            Index.append(i)
            
    return Index


#--------------------------------------FUNCTION 5--------------------------------------

def get_hint(hint_1,hint_2,hint_3):
    '''
    This function will display  a hint for the respective word

    Parameters:
        hint_1: A list of hints
        hint_2: A list of hints
        hint_3: A list of hints   
    '''

    #defining global variables
    global mode,hint_count,hintGiven,hint

    #checks if user has already taken a hint
    if hint_count==1:

        #asks the user if he/she needs a hint
        need_hint = input('If you need a hint, type "YES": ')
        
        common.Exit(need_hint)

        
        if need_hint.upper() == 'YES':
            hintGiven='YES'
            
            #makes hint_count=0, indicating the user has already taken a hint
            hint_count = 0
            
            #gets the hint according to the respective word
            if mode == 'E':
                hint = hint_1[rand].upper()
            if mode == 'M':
                hint = hint_2[rand].upper()
            if mode == 'H':
                hint = hint_3[rand].upper()
                
        else:
            hintGiven='NO'
            hint=''

        #if a hint is provided, prints the hint    
        if hint:
            print('hint: ',hint)

    #if hint is already given, prints the hint    
    elif hint_count==0:
        hintGiven='YES'
        print('hint: ',hint)
        
    
#--------------------------------------FUNCTION 6--------------------------------------     
    
def find_word(hint_1,hint_2,hint_3):
    '''
    This function will allow the user to guess the word

    Parameters:
        hint_1: A list of hints
        hint_2: A list of hints
        hint_3: A list of hints

    Returns:
        Turns: Contains the number of turns provided
        TurnsUsed: Contains the number of turns used
        hintGiven: Contains a yes/no stating if a hint was provided or not
        result: Contains win/loss stating if the user won or lost in the game
    
    '''

    #Assigning global variables
    global Index,guessed,word,hidden_word_list,hint_count

    #Assigning variables
    tries = len(word)
    Turns=len(word)
    stop = 'no'
    guessed=[]
    hint_count=1
    hidden_word = ''.join(hidden_word_list)
    result=''
    

    print()

    #Prints the number of letters the word has
    print('The word has',len(word),'letters')
    
    while stop == 'no':

        #Checks if the word guessed by the user matches the exact word
        if hidden_word == word:

            #Turns used is the number of turns provided minus the tries remaining
            TurnsUsed=Turns-tries
            tries = 0
            print()

            #displays the congratulations message
            print('Congratulations!!\nYou have guessed the word\n\nThe word is: ',word)
            result = 'WIN'
            stop = 'yes'

        #checks if all the tries have exhausted    
        elif tries == 0:
            print()

            #displays the message that the user has lost
            print('Sorry you have run out of tries!\n\nThe word is: ',word)
            result = 'LOSS'
            stop = 'yes'
            TurnsUsed=Turns-tries

        #if the user hasnt won or lost the game continues
        else:

            print()

            #the hidden word with underscores is displayed with a space
            print("  ",' '.join(hidden_word))
            print()
            
            get_hint(hint_1,hint_2,hint_3)
            
            #a letter is taken from the user as a guess     
            guess=input('Enter the letter: ').upper()
            print()
            
            common.Exit(guess)

            #checks if the letter is already guessed
            if guess in guessed:
                print('You have already guessed this letter, letter: ',guess)
                
                #a try is exhausted
                tries -= 1
                print('You have',tries,'tries remaining')

            #checks if the input is not a letter, or if it is a blank value
            elif common.is_letter(guess) == False or guess == '' :
                print('Invalid input')

            #checks if the guessed letter is not in the word
            elif guess not in word:
                print('Wrong guess!')
                
                #the guessed letter is appended to the list of guessed letters
                guessed.append(guess)

                #a try is exhausted
                tries -= 1
                
                print('You have',tries,'tries remaining')

            #checks if the guessed letter is in the word
            elif guess in word:
                print('Correct guess!')

                #the guessed letter is appended to the list of guessed letters
                guessed.append(guess)

                #finds the index of the guessed letter in the word
                I=(find_index(word,guess))

                #replaces the underscore with the respective guessed letter
                for i in (I):
                    hidden_word_list[i]=guess
                hidden_word = ''.join(hidden_word_list)
                
                if hidden_word == word:
                    print()
                else:
                    print('You have',tries,'tries remaining')
    
    return Turns,TurnsUsed,hintGiven,result


    



            



        
        


    
