from random import randint
import sys
import os
import time


run = True
game_info = None


# prints saved to variables
def make_hangman(level):
    """making list of hangman ASCII draws, based on difficulty_level, for"""
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
    if level == "HARD":
        hangman_draw = [stage0_print, stage1_print, stage2_print, stage3_print,
                        stage4_print, stage5_print, stage6_print, stage7_print,
                        stage8_print, stage9_print, stage10_print,
                        stage11_print, ""]
    elif level == "EASY":
        hangman_draw = [stage0_print, stage6_print, stage7_print,
                        stage9_print, stage10_print, ""]
    return hangman_draw


def choose_level():
    """reading user input for choosing level.
       Returns a 'game_info' dictionary, which contains initial information"""
    loop = True
    while loop:  # loop is forcing user to enter E or H to chose a level
        difficulty_level = input("Enter \"E\" to play easy (only European "
                                 "capitols, 5 tries) or \"H\" to play hard "
                                 "(whole World, 12 tries): ").upper()
        if difficulty_level == "H":
            difficulty_level = "HARD"  # changed to ease print and output
            # choosing expected number of records to import from database
            records_to_read = 183
            life = 12  # choosing number of lives
            loop = False  # end loop
        elif difficulty_level == "E":
            difficulty_level = "EASY"
            records_to_read = 45
            life = 5
            loop = False
    game_info = {"difficulty_level": difficulty_level,
                 "records_to_read": records_to_read,
                 "hangman_draw": make_hangman(difficulty_level),
                 "life": life}
    return game_info


def read_database(records_to_read):
    """reading database file. given expected number of records,
       returns 'records' list"""
    try:
        # importing database form file. file should be in same directory as .py
        with open("./countries_and_capitals.txt", 'r') as db_file:
            records = []
            for i, line in zip(range(1, records_to_read + 1), db_file):
                # making a list from each line from the file
                line = line.strip()
                # making list 'line' which contains two elements: 'country' and 'capital'
                line = line.split(' | ')
                records.append(line)
    except FileNotFoundError:
        sys.exit("Error: Missing database.\nMake sure you placed "
                 "'countries_and_capitals.txt' file in same directory as "
                 ".py file")
    return records


def draw_secret_word(records_to_read):
    """drawing random position of database, given expected number of records,
       returns tuple of capitol and country"""
    lines_list = read_database(records_to_read)
    # when we got problems with database (our database is too short)
    # program should choose maximum possible records from database
    if records_to_read > len(lines_list):
        records_to_read = len(lines_list)
        print("Problem with database.\nProgram is not fully operational.")
    # choosing random index in range based on difficulty_level
    random_index = randint(0, records_to_read)
    secret_word = lines_list[random_index][1].upper()
    country_name = lines_list[random_index][0].upper()
    return (secret_word, country_name)


def make_hidden_word(secret_word_list):
    """making dash copy of given list. returns list"""
    hidden_word_list = []
    for i in range(len(secret_word_list)):
        # replacing only letters, other char remains the same
        if secret_word_list[i].isalpha():
            hidden_word_list.append("_")
        else:
            hidden_word_list.append(secret_word_list[i])
    return hidden_word_list


def read_guess():
    """reading user input and force user to make proper input. returns string 'guess'."""
    try:
        # loop is working until correct char is entered (ignores other char)
        loop = True  # reset 'loop' for every new letter user is guessing
        while loop:
            guess = (input("\nEnter letter, or try to guess whole word at once"
                           " ('help' for tip): ")).upper()
            guess = guess.replace(" ", "")
            loop = not guess.isalpha()
            if loop:
                print("It's not a letter!\n")
    except (EOFError, KeyboardInterrupt):
        sys.exit("\nYou have exited the game\nThanks for playing!")
    return guess


def make_summary():
    """making summary of game, updating game_info dictionary and print results"""
    global game_info
    player_name = None
    # when user lose a game
    if game_info["life"] == 0:
        print(game_info['hangman_draw'][game_info["life"]])
        print("\nGAME OVER\nThe capital you were looking for was " +
              game_info['secret_word'] + ".\nIt's a capital of " +
              game_info['country_name'] + ".")
    # when user win a game
    else:
        score = calculate_score(game_info)
        print("\n", game_info['secret_word'].upper())
        print("\nYou guessed!\n" + game_info['secret_word'] +
              " is a capital of " + game_info['country_name'] + ".")
        print("\nYou guessed after ", game_info['ask_numbers'],
              " letters\nIt took you ", game_info['game_time'], "sec.")
        print("Your score is: ", score, " points.")
        while player_name is None:
            try:
                player_name = input('\nPlease enter your name: ')
            except (EOFError, KeyboardInterrupt):
                pass
            game_info["player_name"] = player_name
            game_info["score"] = score
        save_score(game_info)
    return


def calculate_score(game_info):
    """calculating player's score. usues dictinary with all stored game info,
       returns score. alghoritm may by changed in future basing on UX ;)"""
    score = int(150 - 0.5
                * game_info["game_time"]
                - game_info["ask_numbers"]
                * 5 - game_info["tip"] * 20)
    if game_info["difficulty_level"] == "HARD":
        score *= 1.3  # for hard mode score is multiplied by 1.3
    if score < 0:  # to avoid negative numbers in scoring
        score = 0
    return score


def save_score(game_info):
    """saving players score and some game info to file"""
    today = str(time.strftime('%Y-%m-%d'))
    now = str(time.strftime('%H:%M:%S'))
    # creating tuple of all data needed to be stored in highscore file
    score = (game_info["player_name"], today, now,
             game_info["difficulty_level"], game_info['secret_word'],
             game_info["score"])
    # making record to save in file
    score_formated = []
    for item in score:
        item = str(item)
        # every column should be exactly 10 char long so if item is to short
        # we add spaces, if to long we trim it
        if len(item) < 10:
            item = item + ((10-len(item)) * " ")
        elif len(item) == 10:
            pass
        else:
            item = item[:-(len(item)-10)]
        score_formated.append(item)
    score_formated = ' | '.join(score_formated)
    # writing created record to file
    highscore_file = open("./high_score.txt", 'a')
    highscore_file.write(score_formated + "\n")


def show_high_score():
    """importing highscore table from file and print it"""
    try:
        highscore_file = open("./high_score.txt", 'r')
        highscore_list = []  # list of scorelines from score file
        for line in highscore_file:  # importing record(each line) from file
            line = line.strip()
            # changing imported record to list (needed to sort by score)
            line = line.split(' | ')
            for item in line:  # triming spaces in elements
                item.split()
            highscore_list.append(line)  # making list of records (list of lists)
        # sorting by 5th element of each list(scoring)
        # lambda is a function which returns 5th element of record
        # when called with argument record
        highscore_list = sorted(highscore_list, key=lambda record: int(record[5]),
                                reverse=True)
        # if highscore_list is shorter than 10 records, we print all of them
        print("\nHIGHSCORES:\n")
        if len(highscore_list) < 10:
            for i in range(len(highscore_list)):
                print(' | '.join(highscore_list[i]))
        # if highscore_list is at list 10 records we print first 10
        else:
            for i in range(10):
                print(' | '.join(highscore_list[i]))
    except(ValueError, IndexError):
        print("Error ocured while reading highscores file\n")


def restart():
    """restarting program. read user input, returns boolean 'run'"""
    restart = input("\nEnter \"P\" if you want to play again\n")
    if restart.upper() == "P":
        run = True
    else:
        print("\nYou have exited the game\nThanks for playing!")
        run = False
    return run


def main():
    global game_info
    game_info = choose_level()
    secret_record = draw_secret_word(game_info["records_to_read"])
    game_info["secret_word"] = secret_record[0]
    game_info["country_name"] = secret_record[1]
    secret_word_list = list(secret_record[0])
    hidden_word_list = make_hidden_word(secret_word_list)
    game_info["ask_numbers"] = 0
    game_info["tip"] = 0
    not_in_word = []
    start_time = time.time()

    # loop is working until game is on (user neither win nor lose)
    while game_info["life"] > 0 and hidden_word_list != secret_word_list:
        print("\n", ' '.join(hidden_word_list))
        print(game_info['hangman_draw'][game_info["life"]])
        print("\nLevel:", game_info["difficulty_level"],
              "Life:", game_info["life"])
        if len(not_in_word) > 0:
            print("Not in word:", not_in_word)
        guess = read_guess()

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
                game_info["life"] -= 1
            game_info["ask_numbers"] += 1

        # guessing whole world
        else:
            # guessed
            if guess == game_info["secret_word"].replace(" ", ""):
                hidden_word_list = secret_word_list
            # asked for tip
            elif guess == "HELP":
                game_info["tip"] += 1  # used for scoring
                print("\nCapital city of ", game_info['country_name'])
            # failed
            else:
                if game_info["life"] == 1:
                    game_info["life"] -= 1
                else:
                    game_info["life"] -= 2
    game_info["game_time"] = int(time.time() - start_time)


while run:  # runs once a game, when restart, runs again
    try:
        os.system('clear')  # clears screen before game
        main()
        make_summary()
        show_high_score()
        run = restart()
    except (EOFError, KeyboardInterrupt):
        sys.exit("\nYou have exited the game\nThanks for playing!")
