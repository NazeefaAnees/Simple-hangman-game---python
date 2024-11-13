#---------------------------------IMPORT MODULES----------------------------------
#user modules
import modules.game_hist as game_hist
import modules.common as common


#----------------------------------DEFINING FUNCTIONS----------------------------------
#--------------------------------------FUNCTION 1-------------------------------------- 

def stats():
    '''
    This function will get the Total games played, Total losses and wins

    Returns:
        TotalGames: This contains the value of the total number of games played
        TotalWins: This contains the value of the total number of wins
        TotalLoss: This contains the total number of losses 
    '''
    
    while True:
        
        #Assigning variable(empty)
        choice=0
        c=0

        #exception handling
        try :
            #displaying a mini menu system to get the choice from the user
            print('\n\n')
            print('I want to view the stats for:')
            print('1. The whole game history')
            print('2. This session')
            print()

            #getting the choice from the user
            c=input('Enter your choice: ')
            common.Exit(c)
            choice=int(c)
            common.clearConsole()

        #raises an error if a value other than an integer is input    
        except ValueError:
            print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
            common.clearConsole()
            continue
        else:
            #executes the function for choice1
            if choice==1:

                #opens the database
                db=game_hist.open_db()

                #prepare a cursor object using cursor() method
                cursor=db.cursor()

                #executing SQL query to display all the data from the table
                cursor.execute('SELECT * FROM playerinfo')
                
                data=cursor.fetchall()
                TotalGames=cursor.rowcount

                #executing SQL query to display all the data from the table according to a condition
                cursor.execute('SELECT * FROM playerinfo WHERE winORloss="WIN"')
                
                data=cursor.fetchall()
                TotalWins=cursor.rowcount

                #executing SQL query to display all the data from the table according to a condition
                cursor.execute('SELECT * FROM playerinfo WHERE winORloss="LOSS"')
                
                data=cursor.fetchall()
                TotalLoss=cursor.rowcount

                break
            
            elif choice==2:
                #executes the functions for choice2
                db=game_hist.open_db()
                cursor=db.cursor()

                #executing SQL query to display all the data from the table
                cursor.execute('SELECT * FROM playerinfo_persession')
                
                data=cursor.fetchall()
                TotalGames=cursor.rowcount

                #executing SQL query to display all the data from the table according to a condition
                cursor.execute('SELECT * FROM playerinfo_persession WHERE winORloss="WIN"')
                
                data=cursor.fetchall()
                TotalWins=cursor.rowcount

                #executing SQL query to display all the data from the table according to a condition
                cursor.execute('SELECT * FROM playerinfo_persession WHERE winORloss="LOSS"')
                
                data=cursor.fetchall()
                TotalLoss=cursor.rowcount

                break

            #displays an error message if a wrong integer is entered
            else:
                print('\nINVALID INPUT!!\nPlease enter a valid value!!\n')
                common.clearConsole()
                continue
    

    return TotalGames,TotalWins,TotalLoss


#--------------------------------------FUNCTION 2--------------------------------------

def html():
    '''This function will display the stat data in an html file'''

    #importing built in modules
    import webbrowser

    #getting the variable values from the function
    TotalGames,TotalWins,TotalLoss=stats()

    #opening an html file in write mode
    f=open('game_stats.html','w')

    #assigning the html code to a variable
    html_code=f'''<html>
    <head>
    <title>Hangman game stats</title>
    </head>
    </br>
    <body style="background-color:#0D306E;">

    <h1 style="background-color:#6D7C95;"><center><font face="Arial" color="White" size="10">Hangman stats
    </font><center></h1>


    </br>
    <h2><font face="Arial" color="White" size="5">Total Number of games:    %s </font></h2>
    <h2><font face="Arial" color="White" size="5">Total Number of wins:     %s</font></h2>
    <h2><font face="Arial" color="White" size="5">Total Number of losses:   %s</font></h2>


    </body>
    </html>'''

    #inserting the python variables to the html code
    final=html_code % (TotalGames,TotalWins,TotalLoss)

    #writing the html code into the html file
    f.write(final)

    #closing the html file
    f.close()


    #displaying the stats 
    print('\t---------------------------------------')
    print('\t     STATS FOR THE HANGMAN GAME')
    print('\t---------------------------------------')

    print('\t|Total Games played :   ',TotalGames)
    print('\t|Total Wins:            ',TotalWins)
    print('\t|Total Losses:          ',TotalLoss)

    #opening the html file which contains the stats
    webbrowser.open('game_stats.html')

    









    
