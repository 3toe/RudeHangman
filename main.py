# Hangman game inside console

import random

print("\nWelcome to hangman, bitches!\n")

# Enter player names, prevent duplicate names.
P1 = input("Player 1, please enter your name: ")
if P1 == "Shitbag":
    P1 = "Poopcake"
    print("Congratulations, you've found the one name that Player 1 is not allowed to choose. You will henceforth be "
          "known as \"Poopcake.\"")
P2 = input("Player 2, please enter your name: ")
if P1 == P2:
    P2 = "Shitbag"
    print("Since Player 2 tried to copy Player 1's name, Player 2 has been named \"Shitbag\"")
players = (P1, P2)

# Randomize who goes first for the first game.
First_player = random.choice(players)
if First_player == P1:
    Second_player = P2
else:
    Second_player = P1

# initialize the game count
game_count = 1
# initialize "play again?" flag
play_again = True

while play_again:  # main loop
    # Ask first player to guess a word, and alternate between players until a valid word is chosen
    if game_count == 1:
        word_to_guess = input(First_player + " has been randomly chosen to pick a word! " + Second_player + ", avert "
                              "your eyes while " + First_player + " types it in now. Do not use any numbers, spaces or "
                              "special characters, then hit \"enter\": ").lower()
    else:
        First_player, Second_player = Second_player, First_player  # alternate player's roles for subsequent games.
        print("_______________\nGAME " + str(game_count) + ". Get the fuck ready.\n")
        word_to_guess = input("\n" + First_player + " OK, now it's your turn to pick a word! " + Second_player + ", "
                              "avert your eyes while " + First_player + " types it in now. Do not use any numbers, "
                              "spaces or special characters, then hit \"enter\": ").lower()
    while True:  # swap player roles if the active player chooses an invalid word
        if word_to_guess.isalpha():
            break
        First_player, Second_player = Second_player, First_player
        word_to_guess = input("OK, " + First_player + ", since " + Second_player + " can't follow the rules, you try "
                              "it. Again, no numbers, spaces or special characters: ").lower()

    # Show word as replaced by underscores
    guessed_word = "_"*len(word_to_guess)
    print("\n"*40,"Here's the word: " + guessed_word + "\n")

    # create lists to do letter-guess matching loops
    word_to_guess_list = list(word_to_guess)
    guessed_word_list = list(guessed_word)

    # initialize flag to see if a user has guessed an invalid entry yet (game will disqualify a player if more than one
    # non-letter is chosen.
    guessed_number = False

    # initialize "guessed yet?" flag to give the player a first message upon the first guess, then loop through the same
    # message on all subsequent guesses.
    guess_yet = False

    # Set bad guess counter to 0.
    bad_guesses = 0

    # initialize lists for hit and missed letter guesses
    missed_letters = []

    # main guess loop
    while "_" in guessed_word and bad_guesses < 7:  # as long as the word isn't guessed and the hangman is partial...
        hit_flag = False    # initialize "correct guess" flag to false
        if not guess_yet:   # prompt for the first letter guess of the game.
            letter_guess = input("OK, " + Second_player + ", guess a letter, then hit enter: ").lower()
            guess_yet = True
        else:   # The prompt for every other guess in the game.
            print("\nThe word so far is " + guessed_word + "\nIncorrect guesses: ", *missed_letters, "\n")
            letter_guess = input(Second_player + ", pick another letter (or you can try to guess the whole word), then "
                                                 "hit enter: ").lower()
        if letter_guess == word_to_guess:  # end game if player guesses the full word correctly
            break
        if (len(letter_guess) != 1 and len(letter_guess) != len(word_to_guess)) or not letter_guess.isalpha():
            # catch and warn for invalid guesses. don't end game if player attempts a full word guess but is wrong.
            if not guessed_number:
                guessed_number = True  # set "invalid guess" flag to true, so that the next invalid guess ends the game
                letter_guess = input("Only warning, enter a SINGLE LETTER or the whole word. no numbers nor symbols, and "
                                     "hit \"enter\": ").lower()
                if letter_guess == word_to_guess:  # end game if player guesses the full word correctly
                    break
                if (len(letter_guess) != 1 and len(letter_guess) != len(word_to_guess)) or not letter_guess.isalpha():
                    # end the game with a special error if 2 invalid guesses are made.
                    bad_guesses = 666
                    break
            else:
                bad_guesses = 666  # end the game if an invalid guess was previously made.
                break
        x = 0   # initialize the variable which will loop through the letter list of the word to guess
        for ltr in word_to_guess_list:  # check the guessed letter against each letter in the word to guess
            if ltr == letter_guess:  # if a correct letter is guessed...
                guessed_word_list[x] = letter_guess  # ...update the displayed word...
                hit_flag = True  # ...and set the hit flag True
            x += 1  # check the whole word
        guessed_word = ''.join(guessed_word_list)  # combine the list to display the current state of the word to guess
        if not hit_flag:  # if wrong, display various states of hangman guy (based on number of wrong guesses)
            print("________________\nThat ain't right")
            if len(letter_guess) == 1:
                missed_letters.append(letter_guess)
            bad_guesses += 1
            if bad_guesses == 1:
                print('''
                _____
                |   |
                |   O
                |
                |
                |
               _|______
               |_YOU^_|''')
            if bad_guesses == 2:
                print('''
                _____
                |   |
                |   O
                |   |
                |
                |
               _|______
               |_YOU^_|''')
            if bad_guesses == 3:
                print('''
                _____
                |   |
                |   O
                |  /|
                |
                |
               _|______
               |_YOU^_|''')
            if bad_guesses == 4:
                print('''
                _____
                |   |
                |   O
                |  /|\\
                |
                |
               _|______
               |_YOU^_|''')
            if bad_guesses == 5:
                print('''
                _____
                |   |
                |   O
                |  /|\\
                |   |
                |
               _|______
               |_YOU^_|''')
            if bad_guesses == 6:
                print('''
                _____
                |   |
                |   O
                |  /|\\
                |   |
                |  /
               _|______
               |_YOU^_|''')
            if bad_guesses == 7:
                print('''
                _____
                |   |
                |   O
                |  /|\\
                |   |
                |  / \\
               _|______
               |_YOU^_| ''')
                print("\nAww you died, how morbid.  Why is this such a high-stakes game anyways? Frankly to me it \n"
                      "seems completely absurd to kill someone for not being able to guess all the letters in some \n"
                      "random word, and not to mention, in a way that in this day and age, is going to raise some \n"
                      "eyebrows to say the least. " + First_player + " honestly, you should be ashamed of yourself. \n"
                      "What's the god damn matter with you? Seriously? Anyways, the word was " + word_to_guess + ".")
    if bad_guesses == 666:  # the special error if someone guessed 2 invalid entries.
        print("\nTold you not to be a dumbass again. You lose. And you're a dumbass.\n")
        print("Here hangs " + Second_player + ''' the dumbass (see below)
                _____
                |   |
                |   O
                |  /|\\
                |   |
                |  / \\
               _|______
               |______| ''')
    if bad_guesses < 7: # success message
        print("\nThe word was indeed \"" + word_to_guess + "\". Fuck ya dood!\n")
    y_or_n = input("Do you two clowns want to play again? ")  # ask users if they'd like to play again
    if y_or_n in ["n", "no"]:
        play_again = False  # if not, set flag to stop the main while loop
    else:
        game_count += 1  # otherwise increment the game counter and restart the main loop
