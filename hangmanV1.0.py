from random import randint
import sys
import os
import time
from datetime import datetime

<<<<<<< HEAD
# prints saved to variables
=======
#prints saved to variables
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
stage0_print = """
    _________
    |   |   |
    |   o   |
    |  / \  |
    |   |   |
    |  / \  |
   /|       |\ """

stage1_print = """
    _________
    |   |   |
    |   o   |
    |  / \  |
    |   |   |
    |  /    |
   /|       |\ """

stage2_print = """
    _________
    |   |   |
    |   o   |
    |  / \  |
    |   |   |
    |       |
   /|       |\ """

stage3_print = """
    _________
    |   |   |
    |   o   |
    |  / \  |
    |       |
    |       |
   /|       |\ """

stage4_print = """
    _________
    |   |   |
    |   o   |
    |  /    |
    |       |
    |       |
   /|       |\ """


stage5_print = """
    _________
    |   |   |
    |   o   |
    |       |
    |       |
    |       |
   /|       |\ """

stage6_print = """
    _________
    |   |   |
    |       |
    |       |
    |       |
    |       |
   /|       |\ """

stage7_print = """
    _________
    |       |
    |       |
    |       |
    |       |
    |       |
   /|       |\ """

stage8_print = """
    _________
    |       |
    |       |
    |       |
    |       |
    |       |
   /|       |  """

stage9_print = """
    _________
    |
    |
    |
    |
    |
   /|          """

stage10_print = """

    |
    |
    |
    |
    |
   /|          """

stage11_print = """

    |
    |
    |
    |
    |
    |          """


<<<<<<< HEAD
while True:  # 'main loop' runs once a game, when restart, runs again
=======
while True:#'main loop' runs once a game, when restart, runs again
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
    secret_word_list = []
    hidden_word_list = []
    not_in_word = []
    player_name = None
    tip = 0
<<<<<<< HEAD
    ask_numbers = 0  # number of letters user tries to guess

    os.system('clear')  # clears screen before game

    try:
        #  oop is forcing user to enter E or H to chose a level
        loop = True
        while loop is True:
            difficulty_level = input("""Enter \"E\" to play in easy (only European capitols, 5 tries) mode or \"H\" to play hard (whole World, 12 tries): """).upper()
            if difficulty_level == "H":
                difficulty_level = "HARD"  # changed to ease print and output
                question_base = 183  # choosing number of text lines to import from database
                # choosing specified draws to list, depends on lives quantity
                hangman_draw = [stage0_print, stage1_print, stage2_print, stage3_print,
                                stage4_print, stage5_print, stage6_print, stage7_print,
                                stage8_print, stage9_print, stage10_print, stage11_print, ""]
                life = 12  # choosing number of lives
                loop = False  # end loop
=======
    ask_numbers = 0 #number of letters user tries to guess

    os.system('clear') #clears screen before game

    try:
        #loop is forcing user to enter E or H to chose a level
        loop = True
        while loop == True:
            difficulty_level = input("Enter \"E\" to play in easy " +
                                     "(only European capitols, 5 tries) mode " +
                                     "or \"H\" to play hard (whole World, 12 tries): ").upper()
            if difficulty_level == "H":
                difficulty_level = "HARD" #changed to ease print and output
                question_base = 183 #choosing number of text lines to import from database
                hangman_draw = [stage0_print, stage1_print, stage2_print, stage3_print, stage4_print, stage5_print, stage6_print, stage7_print, stage8_print, stage9_print, stage10_print, stage11_print, ""] #choosing specified draws to list, depends on lives quantity
                life = 12 #choosing number of lives
                loop = False #end loop
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
            elif difficulty_level == "E":
                difficulty_level = "EASY"
                question_base = 45
                hangman_draw = [stage0_print, stage6_print, stage7_print, stage9_print, stage10_print, ""]
                life = 5
                loop = False
    except (EOFError, KeyboardInterrupt):
<<<<<<< HEAD
        sys.exit("\nYou have exited the game\nThanks for playing!")

    try:
        # importing database form file. file should be in same directory as .py and contain
        with open("./countries_and_capitals.txt", 'r') as f:
            lines_list = []  # list containing imported and processed items made of pairs of countries and capitals
            for i, line in zip(range(1, question_base + 1), f):
                line = line.strip()  # making a list from each line from the file, also deleting /n
                line = line.split(' | ')  # making list 'line' which contains two elements: 'country' and 'capital'
                lines_list.append(line)  # making 'lines_list' which contains 'lines' (which are also lists)
            if question_base > len(lines_list):  # when we got problems with database - our database is too short program should choose maximum possible records from database
                question_base = len(lines_list)
                print ("Problem with database.\nProgram is not fully operational.")
            random_index = randint(0, question_base)  # choosing random index in range based on difficulty_level
            secret_word = lines_list[random_index][1].upper()  # importing country name
            country_name = lines_list[random_index][0].upper()  # importing capital name
    except FileNotFoundError:
        sys.exit("Error: Missing database.\nMake sure you placed 'countries_and_capitals.txt' file in same directory as .py file")
    # changes string to list of its characters
    for char in secret_word:
        secret_word_list.append(char)

    # making hidden word as list (as long as original secret_word_list) by adding _ for every char in secret world list
=======
        sys.exit ("\nYou have exited the game\nThanks for playing!")

    try:
        #importing database form file. file should be in same directory as .py and contain
        with open("./countries_and_capitals.txt", 'r') as f:
            lines_list = [] #list containing imported and processed items made of pairs of countries and capitals
            for i , line in zip(range(1 , question_base + 1) , f):
                line = line.strip() #making a list from each line from the file, also deleting /n
                line = line.split(' | ') #making list 'line' which contains two elements: 'country' and 'capital'
                lines_list.append(line) #making 'lines_list' which contains 'lines' (which are also lists)
            if question_base > len(lines_list): #when we got problems with database - our database is too short program should choose maximum possible records from database
                question_base = len(lines_list)
                print ("Problem with database.\nProgram is not fully operational.")
            random_index = randint(0, question_base) #choosing random index in range based on difficulty_level
            secret_word = lines_list[random_index][1].upper() #importing country name
            country_name = lines_list[random_index][0].upper() #importing capital name
    except FileNotFoundError:
        sys.exit ("Error: Missing database.\nMake sure you placed 'countries_and_capitals.txt' file in same directory as .py file")
    #changes string to list of its characters
    for char in secret_word:
        secret_word_list.append (char)

    #making hidden word as list (as long as original secret_word_list) by adding _ for every char in secret world list
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
    for i in range(len(secret_word_list)):
        if secret_word[i].isalpha():
            hidden_word_list.append("_")
        else:
            hidden_word_list.append(secret_word_list[i])

<<<<<<< HEAD
    # before guessing starts we're saving date and time of start
=======
    #before guessing starts we're saving date and time of start
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
    start_time = time.time()
    today = str(time.strftime('%Y-%m-%d'))
    now = str(time.strftime('%H:%M:%S'))

<<<<<<< HEAD
    # loop is working until game is on (user neither win nor lose)
    while life > 0 and hidden_word_list != secret_word_list:
        print ("\n", ' '.join(hidden_word_list))
        print (hangman_draw[life])
        print ("\nLevel:", difficulty_level, "Life:", life)
        if len(not_in_word) > 0:
            print ("Not in word:", not_in_word)
        try:
            # loop is working until correct char is entered (ignores other char)
            loop = True  # reset 'loop' for every new letter user is guessing
            while loop is True:  # or guess.isspace():
                guess = (input("\nEnter letter, or try to guess whole word at once ('help' for tip): ")).upper()
                guess = guess.replace(" ", "")
                loop = not (guess.isalpha())
                if loop is True:
                    print ("It's not a letter!\n")
        except (EOFError, KeyboardInterrupt):
            sys.exit("\nYou have exited the game\nThanks for playing!")
        # guessing a letter
        if len(guess) == 1:
            # guessed
            if guess in secret_word_list:
                for i in range(len(secret_word_list)):
                    if guess == secret_word_list[i]:
                        hidden_word_list[i] = secret_word_list[i]
            # failed
            else:
                not_in_word.append(guess)
                life -= 1
            ask_numbers += 1
        # guessing whole world
        else:
            # guessed
            if guess == secret_word.replace(" ", ""):
                hidden_word_list = secret_word_list
            # asked for tip
            elif guess == "HELP":
                tip += 1  # used for scoring
                print ("\nCapital city of ", country_name)
            # failed
            else:
                if life == 1:
                    life -= 1
                else:
                    life -= 2
    # when user lose a game
    if life == 0:
        print (hangman_draw[life])
        print ("\nGAME OVER\nThe capital you were looking for was " +
               secret_word + ".\nIt's a capital of " + country_name + ".")
    # when user win a game
    else:
        game_time = int(time.time() - start_time)  # time between start and correct answer
        # calculating player's score. alghoritm may by changed in future basing on UX ;)
        if difficulty_level == "EASY":  # for easy mode
            scoring = int(150 - 0.5 * game_time - ask_numbers * 5 - tip * 20)
        else:  # for hard mode (multiplied by 1.3)
            scoring = int((150 - 0.5 * game_time - ask_numbers * 5 - tip * 20)*1.3)
        if scoring < 0:  # to avoid negative numbers in scoring
            scoring = 0
        print ("\n", ' '.join(hidden_word_list))
        print ("\nYou guessed!\n" + secret_word + " is a capital of " + country_name + ".")
        print ("\nYou guessed after ", ask_numbers, " letters\nIt took you ", game_time, "sec.")
        print ("Your score is: ", scoring, " points.")
        while player_name is None:
            try:
                player_name = input('\nPlease enter your name: ')
            except (EOFError, KeyboardInterrupt):
                pass

        # creating tuple of all data needed to be stored in highscore file
        scoreline = player_name, today, now, difficulty_level, secret_word, scoring
        # creating a record (line) to be saved in highscore file

        # making record to save in file
        current_scorelist = []
        for item in scoreline:
            item = str(item)
            # every column should be exatly 10 char long so if item is to short we add spaces if to long we trim it
            if len(item) < 10:
=======
    #loop is working until game is on (user neither win nor lose)
    while life > 0 and hidden_word_list != secret_word_list:
        print ("\n" , ' '.join(hidden_word_list))
        print (hangman_draw[life])
        print ("\nLevel:" , difficulty_level , "Life:" , life)
        if len(not_in_word) > 0:
            print ("Not in word:" , not_in_word)
        try:
            #loop is working until correct char is entered (ignores other char)
            loop = True #reset 'loop' for every new letter user is guessing
            while loop == True: # or guess.isspace():
                guess = (input("\nEnter letter, or try to guess whole word at once ('help' for tip): ")).upper()
                guess = guess.replace(" ","")
                loop = not (guess.isalpha())
                if loop == True:
                    print ("It's not a letter!\n")
        except (EOFError, KeyboardInterrupt):
            sys.exit ("\nYou have exited the game\nThanks for playing!")
        #guessing a letter
        if len(guess) == 1:
            #guessed
            if guess in secret_word_list:
                for i in range (len(secret_word_list)):
                    if guess == secret_word_list[i]:
                        hidden_word_list[i] = secret_word_list[i]
            #failed
            else:
                not_in_word.append (guess)
                life -= 1
            ask_numbers += 1
        #guessing whole world
        else:
            #guessed
            if guess == secret_word.replace(" ",""):
                hidden_word_list = secret_word_list
            #asked for tip
            elif guess == "HELP":
                tip +=1 #used for scoring
                print ("\nCapital city of " , country_name)
            #failed
            else:
                if life == 1:
                    life -=1
                else:
                    life -=2
    #when user lose a game
    if life == 0:
        print (hangman_draw[life])
        print ("\nGAME OVER\nThe capital you were looking for was " + secret_word + ".\nIt's a capital of " + country_name + ".")
    #when user win a game
    else:
        game_time = int(time.time() - start_time)#time between start and correct answer
        #calculating player's score. alghoritm may by changed in future basing on UX ;)
        if difficulty_level == "EASY": #for easy mode
            scoring = int(150 - 0.5 * game_time - ask_numbers * 5 - tip * 20)
        else: #for hard mode (multiplied by 1.3)
            scoring = int((150 - 0.5 * game_time - ask_numbers * 5 - tip * 20)*1.3)
        if scoring < 0:#to avoid negative numbers in scoring
            scoring = 0
        print ("\n" , ' '.join(hidden_word_list))
        print ("\nYou guessed!\n" + secret_word + " is a capital of " + country_name + ".")
        print ("\nYou guessed after " , ask_numbers , " letters\nIt took you " , game_time , "sec.")
        print ("Your score is: " , scoring , " points.")
        while player_name == None:
            try:
                player_name = input ('\nPlease enter your name: ')
            except (EOFError, KeyboardInterrupt):
                pass

        #creating tuple of all data needed to be stored in highscore file
        scoreline = player_name, today, now, difficulty_level, secret_word, scoring
        #creating a record (line) to be saved in highscore file

        #making record to save in file
        current_scorelist = []
        for item in scoreline:
            item = str(item)
            #every column should be exatly 10 char long so if item is to short we add spaces if to long we trim it
            if len(item)<10:
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
                item = item + ((10-len(item)) * " ")
            elif len(item) == 10:
                pass
            else:
                item = item[:-(len(item)-10)]
            current_scorelist.append(item)
        current_score = ' | '.join(current_scorelist)

<<<<<<< HEAD
        # writing created record to file
        f = open("./high_score.txt", 'a')
        f.write(current_score + "\n")

        try:
            # printing top 10 scores
            f = open("./high_score.txt", 'r')
            scorelist = []  # list of scorelines from score file
            for line in f:  # importing record(each line) from file
                line = line.strip()
                line = line.split(' | ')  # changing imported record to list of elements (needed to sort by score)
                for item in line:  # triming spaces in elements
                    item.split()
                scorelist.append(line)  # making list of records (list of lists)

            # sorting by 5th element of each list(scoring)
            # sorting: lambda is a function which returns 5th element of record when called with argument record
            scorelist = sorted(scorelist, key=lambda record: int(record[5]), reverse=True)
            # if scorelist is shorter than 10 records, we print all of them
            if len(scorelist) < 10:
                for i in range(len(scorelist)):
                    print (' | '.join(scorelist[i]))
            # if scorelist is at list 10 records we print first 10
=======
        #writing created record to file
        f = open ("./high_score.txt", 'a')
        f.write(current_score + "\n")

        try:
            #printing top 10 scores
            f = open ("./high_score.txt", 'r')
            scorelist = [] #list of scorelines from score file
            for line in f:#importing record(each line) from file
                line = line.strip()
                line = line.split(' | ')#changing imported record to list of elements (needed to sort by score)
                for item in line: #triming spaces in elements
                    item.split()
                scorelist.append(line)#making list of records (list of lists)

            #sorting by 5th element of each list(scoring)
            #sorting: lambda is a function which returns 5th element of record when called with argument record
            scorelist = sorted(scorelist , key=lambda record:int(record[5]) , reverse = True)
            #if scorelist is shorter than 10 records, we print all of them
            if len(scorelist) < 10:
                for i in range(len(scorelist)):
                    print (' | '.join(scorelist[i]))
            #if scorelist is at list 10 records we print first 10
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
            else:
                for i in range(10):
                    print (' | '.join(scorelist[i]))
        except (ValueError, IndexError):
            print ("Error ocured while reading highscores file\n")

<<<<<<< HEAD
    # restart: when user enter 'P' it set loop to True. that makes 'main loop' run again
=======
    #restart: when user enter 'P' it set loop to True. that makes 'main loop' run again
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
    try:
        restart = input("\nEnter \"P\" if you want to play again\n")
        if restart.upper() == "P":
            pass
        else:
            sys.exit("\nYou have exited the game\nThanks for playing!")
    except (EOFError, KeyboardInterrupt):
<<<<<<< HEAD
        sys.exit("\nYou have exited the game\nThanks for playing!")
=======
        sys.exit ("\nYou have exited the game\nThanks for playing!")
>>>>>>> 8409f005d8f1c6bae028efccecca2d3e19253242
