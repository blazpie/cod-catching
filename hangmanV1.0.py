from random import randint
import sys
import os
import time
from datetime import datetime


# prints saved to variables
def make_hangman(level):
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
    #  loop is forcing user to enter E or H to chose a level
    loop = True
    while loop is True:
        difficulty_level = input("Enter \"E\" to play easy (only European "
                                 "capitols, 5 tries) or \"H\" to play hard "
                                 "(whole World, 12 tries): ").upper()
        if difficulty_level == "H":
            difficulty_level = "HARD"  # changed to ease print and output
            # choosing number of text lines to import from database
            question_base = 183
            life = 12  # choosing number of lives
            loop = False  # end loop
        elif difficulty_level == "E":
            difficulty_level = "EASY"
            question_base = 45
            life = 5
            loop = False
    game_info = {"difficulty_level": difficulty_level,
                 "question_base": question_base,
                 "hangman_draw": make_hangman(difficulty_level),
                 "life": life}
    return game_info


def read_database(question_base):
    try:
        # importing database form file. file should be in same directory as .py
        with open("./countries_and_capitals.txt", 'r') as f:
            lines_list = []
            for i, line in zip(range(1, question_base + 1), f):
                # making a list from each line from the file
                line = line.strip()
                # making list 'line' which contains two elements:
                # 'country' and 'capital'
                line = line.split(' | ')
                # making 'lines_list' which contains 'lines' (which are lists)
                lines_list.append(line)
    except FileNotFoundError:
        sys.exit("Error: Missing database.\nMake sure you placed "
                 "'countries_and_capitals.txt' file in same directory as "
                 ".py file")
    return lines_list


def draw_secret_word(question_base):
    lines_list = read_database(question_base)
    # when we got problems with database (our database is too short)
    # program should choose maximum possible records from database
    if question_base > len(lines_list):
        question_base = len(lines_list)
        print("Problem with database.\nProgram is not fully operational.")
    # choosing random index in range based on difficulty_level
    random_index = randint(0, question_base)
    secret_word = lines_list[random_index][1].upper()
    country_name = lines_list[random_index][0].upper()
    return (secret_word, country_name)


def make_hidden_word(secret_word_list):
    hidden_word_list = []
    for i in range(len(secret_word_list)):
        if secret_word_list[i].isalpha():
            hidden_word_list.append("_")
        else:
            hidden_word_list.append(secret_word_list[i])
    return hidden_word_list


def read_guess():
    try:
        # loop is working until correct char is entered (ignores other char)
        loop = True  # reset 'loop' for every new letter user is guessing
        while loop is True:  # or guess.isspace():
            guess = (input("\nEnter letter, or try to guess whole word at once"
                           " ('help' for tip): ")).upper()
            guess = guess.replace(" ", "")
            loop = not (guess.isalpha())
            if loop is True:
                print("It's not a letter!\n")
    except (EOFError, KeyboardInterrupt):
        sys.exit("\nYou have exited the game\nThanks for playing!")
    return guess


def main():
    global game_info
    secret_record = draw_secret_word(game_info["question_base"])
    game_info["secret_word"] = secret_record[0]
    game_info["country_name"] = secret_record[1]
    secret_word_list = list(secret_record[0])
    hidden_word_list = make_hidden_word(secret_word_list)
    game_info["ask_numbers"] = 0
    game_info["tip"] = 0
    not_in_word = []
    start_time = time.time()

    # number of letters user tries to guess

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


def resume(game_info):
    player_name = None
    # when user lose a game
    if game_info["life"] == 0:
        print(game_info['hangman_draw'][game_info["life"]])
        print("\nGAME OVER\nThe capital you were looking for was " +
              game_info['secret_word'] + ".\nIt's a capital of " +
              game_info['country_name'] + ".")
    # when user win a game
    else:
        # time between start and correct answer
        # calculating player's score.
        # alghoritm may by changed in future basing on UX ;)
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
    score = int(150 - 0.5
                * game_info["game_time"]
                - game_info["ask_numbers"]
                * 5 - game_info["tip"] * 20)
    if game_info["difficulty_level"] == "HARD":  # for easy mode
        score *= 1.3
    if score < 0:  # to avoid negative numbers in scoring
        score = 0
    return score


def save_score(game_info):
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
        # we add spaces if to long we trim it
        if len(item) < 10:
            item = item + ((10-len(item)) * " ")
        elif len(item) == 10:
            pass
        else:
            item = item[:-(len(item)-10)]
        score_formated.append(item)
    score_formated = ' | '.join(score_formated)
    # writing created record to file
    f = open("./high_score.txt", 'a')
    f.write(score_formated + "\n")


def show_high_score():
    try:
        # printing top 10 scores
        f = open("./high_score.txt", 'r')
        scorelist = []  # list of scorelines from score file
        for line in f:  # importing record(each line) from file
            line = line.strip()
            # changing imported record to list (needed to sort by score)
            line = line.split(' | ')
            for item in line:  # triming spaces in elements
                item.split()
            scorelist.append(line)  # making list of records (list of lists)
        # sorting by 5th element of each list(scoring)
        # lambda is a function which returns 5th element of record
        # when called with argument record
        scorelist = sorted(scorelist, key=lambda record: int(record[5]),
                           reverse=True)
        # if scorelist is shorter than 10 records, we print all of them
        print("\nHIGHSCORES:\n")
        if len(scorelist) < 10:
            for i in range(len(scorelist)):
                print(' | '.join(scorelist[i]))
        # if scorelist is at list 10 records we print first 10
        else:
            for i in range(10):
                print(' | '.join(scorelist[i]))
    except(ValueError, IndexError):
        print("Error ocured while reading highscores file\n")


def restart():
    restart = input("\nEnter \"P\" if you want to play again\n")
    if restart.upper() == "P":
        run = True
    else:
        print("\nYou have exited the game\nThanks for playing!")
        run = False
    return run


run = True
while run is True:  # 'main loop' runs once a game, when restart, runs again
    try:
        os.system('clear')  # clears screen before game
        game_info = choose_level()
        main()
        resume(game_info)
        show_high_score()
        run = restart()
    except (EOFError, KeyboardInterrupt):
        sys.exit("\nYou have exited the game\nThanks for playing!")
