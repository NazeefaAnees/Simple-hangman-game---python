#---------------------------------IMPORT MODULES----------------------------------
#user modules
import modules.game_hist as game_hist
import modules.common as common

#built-in modules
import mysql.connector
import texttable


#----------------------------------DEFINING FUNCTIONS----------------------------------
#--------------------------------------FUNCTION 1-------------------------------------- 

def open_db():
    '''
    This function will open the database and check the connectivity of the database

    Returns:
        db: contains the database connection
    '''
    
    from mysql.connector import Error

    
    try_again='Y'
    while try_again=='Y':

        #Exception handling
        try:
            #opening the database connection with a dictionary
            conDict={'host':'localhost',
                    'database':'hangman',
                    'user':'root',
                    'password':''}
            db = mysql.connector.connect(**conDict)

            #loop is broken if the database is connected
            if db.is_connected():
                break

        #If an error is encountered,it displays the error
        except Error as e: 
            print('You have encountered an error')

            #prints the error
            print(e)
            
            print('\nPlease connect to the database properly and try again')
            print('You can follow the instructions given in the report on chapter 3.5 page 46')
            print()

            #Asks the user if he/she wants to try again after connecting to the db properly
            while True:
                try_again=input('Enter "Y" to try again or you can exit the program by typing "EXIT": ').upper()
                common.clearConsole()

                #if he wants to try again
                if try_again=='Y':
                    break

                #exits if he wants to exit
                if try_again=='EXIT':
                    common.clearConsole() 
                    raise exit()

                #if input is invalid, asks the user to input a valid value
                else:
                    print()
                    print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
                    
        if try_again=='EXIT':
            common.Exit(try_again)
            break
        
    return db
    

#--------------------------------------FUNCTION 2-------------------------------------- 
    
def datainput(val1,val2,val3,val4,val5,val6,val7,val8,val9):
    '''
    This function will add the details into the database
    
    Parameters:
        val1: a string value which contains the date
        val2: a string value which contains the time
        val3: a string value which contains the name
        val4: a string value which contains the mode
        val5: a string value which contains the word
        val6: an int value which contains the number of turns 
        val7: an int value which contains the number of turns used
        val8: a string value which contains a 'YES' or 'NO' stating if a hint was provided
        val9: a string value stating if it is a 'WIN' or 'LOSS'
        
    '''
    #opens the database
    db=game_hist.open_db()

    #prepare a cursor object using cursor() method
    cursor = db.cursor()
    
    #executing SQL query to insert data into the tables
    query='INSERT INTO playerinfo (date,time,name,mode,word,turns,turnsUsed,hintGiven,winORloss)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val=(val1,val2,val3,val4,val5,val6,val7,val8,val9)

    cursor.execute(query,val)

    #commits the change
    db.commit()

    #disconnects from the server
    db.close()

    
#--------------------------------------FUNCTION 3--------------------------------------
 
def sessionTable():
    '''This function will delete the existing table which records the game history per session'''
    #opens the database
    db=game_hist.open_db()

    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #executing SQL query to delete all the data from the table
    cursor.execute('DELETE FROM playerInfo_perSession')

    #commits the change
    db.commit()

    #disconnects from the server
    db.close()


#--------------------------------------FUNCTION 4--------------------------------------    

def sessionData(val1,val2,val3,val4,val5,val6,val7,val8,val9):
    '''
    This function will create a table and add the details in the table

    Parameters:
        val1: a string value which contains the date
        val2: a string value which contains the time
        val3: a string value which contains the name
        val4: a string value which contains the mode
        val5: a string value which contains the word
        val6: an int value which contains the number of turns 
        val7: an int value which contains the number of turns used
        val8: a string value which contains a 'YES' or 'NO' stating if a hint was provided
        val9: a string value stating if it is a 'WIN' or 'LOSS'
    '''
    #opens the database
    db=game_hist.open_db()

    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #executing SQL query to alter the table by making the auto increment to 1
    cursor.execute('ALTER TABLE playerInfo_perSession AUTO_INCREMENT = 1')

    #commits the change
    db.commit()

    #Executing the SQL query to insert data into the table
    query='INSERT INTO playerInfo_perSession (date,time,name,mode,word,turns,turnsUsed,hintGiven,winORloss)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    val=(val1,val2,val3,val4,val5,val6,val7,val8,val9)

    cursor.execute(query,val)

    #commits the change
    db.commit()

    #disconnects from the server
    db.close()


#--------------------------------------FUNCTION 5-------------------------------------- 

def choice1():
    '''This function will display the game history for the session'''

    #opens the database
    db=game_hist.open_db()

    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #executing SQL query to display all the data from the table
    cursor.execute('SELECT * FROM playerinfo_persession')

    #fetching the data using fetchall() method
    data=cursor.fetchall()

    #counting the number of rows
    row=cursor.rowcount

    #prints 'Sorry there are no entries' if there are no rows found
    if row == 0:
        print('Sorry, There are no entries')

    #displays the data if there are rows found
    else:

        #organizing the data in table format using the texttable module
        table=texttable.Texttable()

        #Creating the heading names for the table
        headings=['ID','Date','Time','Name','Mode','Word','Turns','TurnsUsed','Hint','Status']
        table.header(headings)

        #inserts the rows of data into the table
        for row in data:
            table.add_row(row)
            
        #adjusting column width
        table.set_cols_width([5,15,7,15,8,15,5,5,5,6])

        #content is formatted into a table
        a=table.draw()
        print('\n\n\n\n\n')
        print(a)

        #disconnects from the server
        db.close()

        
#--------------------------------------FUNCTION 6-------------------------------------- 

def choice2():
    '''This function will display the whole game history'''

    #opens the database
    db=game_hist.open_db()

    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #executing SQL query to display all the data from the table
    cursor.execute('SELECT * FROM playerinfo')

    #fetching the data using fetchall() method
    data=cursor.fetchall()

    #counting the number of rows
    row=cursor.rowcount

    #prints 'Sorry there are no entries' if there are no rows found
    if row == 0:
        print('Sorry, There are no entries')

    #displays the data if there are rows found
    else:

        #organizing the data in table format using the texttable module
        table=texttable.Texttable()

        #Creating the heading names for the table
        headings=['ID','Date','Time','Name','Mode','Word','Turns','TurnsUsed','Hint','Status']
        table.header(headings)
        

        #inserts the rows of data into the table
        for row in data:
            table.add_row(row)

        #adjusting column width
        table.set_cols_width([5,15,7,15,8,15,5,5,5,6])

        #content is formatted into a table
        a=table.draw()
        print('\n\n\n\n\n')
        print(a)

        #disconnects from the server
        db.close()
        

#--------------------------------------FUNCTION 7-------------------------------------- 

def choice3():
    '''This function will display the game history of the selected player'''

    #getting the name of the player from the user
    name=input("Enter the player's name to check the game history: ").upper()

    #opens the database
    db=game_hist.open_db()

    #prepare a cursor object using cursor() method
    cursor=db.cursor()

    #executing SQL query to display the data from the table with a condition
    cursor.execute("SELECT * FROM playerinfo WHERE name = '"+str(name)+"' ")

    #fetching the data using fetchall() method
    data=cursor.fetchall()

    #counting the number of rows
    row=cursor.rowcount

    #prints 'Sorry there are no entries' if there are no rows found
    if row == 0:
        print('Sorry, There are no entries')

    #displays the data if there are rows found
    else:

        #organizing the data in table format using the texttable module
        table=texttable.Texttable()

        #Creating the heading names for the table
        headings=['ID','Date','Time','Name','Mode','Word','Turns','TurnsUsed','Hint','Status']
        table.header(headings)

         #inserts the rows of data into the table
        for row in data:
            table.add_row(row)

        #adjusting column width
        table.set_cols_width([5,15,7,15,8,15,5,5,5,6])

        #content is formatted into a table
        a=table.draw()
        print('\n\n\n\n\n')
        print(a)

        #disconnects from the server
        db.close()


#--------------------------------------FUNCTION 8-------------------------------------- 

def view_hist():
    '''This function will display a mini menu for the user to select from which data the user needs to view'''
    
    while True:

        #assigning the variables(empty)
        c=''
        choice=0

        #exception handling
        try:

            #displays the three options for the user to choose from
            print('\n\n')
            print('1. I want to view the game history for this session')
            print('2. I want to view the whole game history')
            print('3. I want to view the game history of a specific player')
            print()

            #asks the user for the choice
            c=input('Enter your choice: ')
            
            common.Exit(c)
            choice=int(c)
            common.clearConsole()
            
        except ValueError:
            #if anything else other than "EXIT" or an integer is given as input, an error message will be displayed
            print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
            common.clearConsole()
            continue

        else:
            #executes the functions for choice1
            if choice==1:
                game_hist.choice1()
                break
            #executes the functions for choice2
            elif choice==2:
                game_hist.choice2()
                break
            #executes the functions for choice3
            elif choice==3:
                game_hist.choice3()
                break
            #displays an error message if a wrong integer is entered
            else:
                print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
                common.clearConsole()
                continue
    
    



















    
    
    
