#This program allows the user to play an advanced, interactive version of Hangman.



import time
import random

#9 Dictionaries to store subject+level-specific words.
easy_technology = [
  'bugs',
  'application',
  'software',
  'traffic',
  'dictionary',
  'hack',
  'caching',
  'router',
  'uptime'
]

medium_technology = [
  'content curation',
  'data mining',
  'artificial intelligence',
  'front end',
  'application',
  'bounce rate',
  'pixels per inch',
  'firewall',
  'cloud computing'
]

hard_technology = [
  'website optimization',
  'click through rate',
  'conversion rate optimization',
  'search engine marketing',
  'virtual private network',
  'relational database management system',
  'integrated development environment',
  'near field communication',
  'responsive web design'
]

easy_geography = [
  'city',
  'atlas',
  'east',
  'key',
  'land',
  'sea',
  'west',
  'south',
  'north'
]

medium_geography = [
  'street map',
  'territory',
  'sea level',
  'weather map',
  'political map',
  'northwest',
  'northeast',
  'longitude',
  'latitude'
]

hard_geography = [
  'azimuth',
  'bathymetric map',
  'cartography',
  'geographic coordinates',
  'international date line',
  'nautical chart',
  'topography',
  'tributary',
  'topographic map'
]

easy_business_and_finance = [
  'asset',
  'liability',
  'profit',
  'loss',
  'loan',
  'value',
  'lien',
  'credit',
  'debit'
]

medium_business_and_finance = [
  'balance sheet',
  'cash flow',
  'collateral',
  'financial statement',
  'credit limit',
  'accrual',
  'expense',
  'wage',
  'tax deduction'
]

hard_business_and_finance = [
  'accounts payable',
  'accounts receivable',
  'income statement',
  'annual percentage rate',
  'debt consolidation',
  'cash flow projection',
  'depreciation',
  'intangible asset',
  'floating interest rate'
  ]

#1 Dictionary to store general hints.
general_hints = [
  'Hint: For almost every word of every length, your best four guesses will be vowels.',
  'Hint: Prepare for longer words in higher difficulty levels.',
  'Hint: Prepare for words that are used less frequently in higher difficulty levels.',
  'Hint: Three of the most common consonants of the English language are R, S and T. ',
  'Hint: In dictionaries, J, Q, and Z are found the least, but some of the words are rarely used. And if you value the opinion of cryptologists (people who study secret codes and communication), X, Q, and Z make the fewest appearances in the writing scene.',
  'Hint: Words that seem more lengthy (large number of blanks) often have 2-3 parts.'
]

general_hint = random.choice(general_hints)

name = input("What is your name? ").title()
rule_review = input("Good day, would you like to review the rules of Hangman prior to playing the game? ").title()
#Code determines whether or not the rules of Hangman must be reviewed based on user's input (above).
while rule_review !=  "Yes" and rule_review != "Y" and rule_review != "No" and rule_review != "N":
  print("That is an invalid input. Try again.")
  rule_review = input(name + ", would you like to review the rules of Hangman prior to playing the game? ").title()
else:
  if rule_review == "Yes" or rule_review == "Y":
    print("\nHere is your rule review: I (the program) will draw up a word or phrase based on the your liking (of subject and difficulty level). You (the guessing player) will try to guess what the word isóone letter at a time. I will draw a number of dashes equivalent to the number of letters in the word. If the you suggest a letter that occurs in the word, then I will fill in the blanks with that letter in the right places. If the word does not contain the suggested letter, I will draw one element of a hangmanís gallows. As the game progresses, a segment of the gallows and a victim is added for every suggested letter not in the word. The number of incorrect guesses before the game ends (regardless of your word) is 6, meaning that you will have 6 incorrect guesses before completing a character in a noose. Once this happens, the game ends and you lose. Should you guess the correct answer before 6 incorrect tries, you will then be the winner of our game. Essentially the objective of the game is for the player to guess letters which correctly fill in the blanks before their little man gets hung out to dry. Regardless of whether you win or lose, an opportunity to play Hangman once more will be given to you. This process will repeat until you choose to no longer play.")
  elif rule_review == "No" or rule_review == "N":
    print("Perfect, you are aware of Hangman's etiquette. Without further adieu, let us begin playing.")

#User decides on difficulty level of their word.
print("\nNext step--> Choose your word! (That is, to a certain extent, of course.)")
user_difficulty = input("What level of difficulty would you like your word to be? [E]asy/[M]edium/[H]ard ").title()

#Repeats invalid option until user enters a given difficulty level
while user_difficulty != 'E' and user_difficulty != 'Easy' and user_difficulty != 'M' and user_difficulty != 'Medium' and user_difficulty != 'H' and user_difficulty != 'Hard':
  print("That is an invalid level of difficulty. Please try again.")
  user_difficulty = input("What level of difficulty would you like your word to be? [E]asy/[M]edium/[H]ard").title()
else:
  print("You have chosen", user_difficulty, "as your difficulty level.")

#User decides on difficulty level of their word.
user_topic = input("What topic would you like your word to relate to? [T]echnology/[G]eography/[B]usiness & Finance ").title()

#Code draws up a wordóbased on user's input of desired topic and difficulty levelóout of the relevant list (each of which contain 9 words) in a random manner. It then converts all letters to uppercase for comparison convenience.
while user_topic != 'T' and user_topic != 'Technology' and user_topic != 'G' and user_topic != 'Geography' and user_topic != 'B' and user_topic != 'Business & Finance':
  print("That is an invalid topic. Please try again.")
  user_topic = input("What topic would you like your world to relate to? [T]echnology/[G]eography/[B]usiness & Finance").title()
else:
  if user_topic == 'T' or user_topic == 'Technology':
    if user_difficulty == 'E' or user_difficulty == 'Easy':
      def get_word():
          word = random.choice(easy_technology)
          return word.upper()
    elif user_difficulty == 'M' or user_difficulty == 'Medium':
      def get_word():
        word = random.choice(medium_technology)
        return word.upper()
    elif user_difficulty == 'H' or user_difficulty == 'Hard':
      def get_word():
        word = random.choice(hard_technology)
        return word.upper()
  if user_topic == 'G' or user_topic == 'Geography':
    if user_difficulty == 'E' or user_difficulty == 'Easy':
      def get_word():
        word = random.choice(easy_geography)
        return word.upper()
    elif user_difficulty == 'M' or user_difficulty == 'Medium':
      def get_word():
        word = random.choice(medium_geography)
        return word.upper()
    elif user_difficulty == 'H' or user_difficulty == 'Hard':
      def get_word():
        word = random.choice(hard_geography)
        return word.upper()
  if user_topic == 'B' or user_topic == 'Business & Finance':
    if user_difficulty == 'E' or user_difficulty == 'Easy':
      def get_word():
        word = random.choice(easy_business_and_finance)
        return word.upper()
    elif user_difficulty == 'M' or user_difficulty == 'Medium':
      def get_word():
        word = random.choice(medium_business_and_finance)
        return word.upper()
    elif user_difficulty == 'H' or user_difficulty == 'Hard':
      def get_word():
        word = random.choice(hard_business_and_finance)
        return word.upper()

def play(word):
    #Represents unguessed letters as underscores.
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    #Number of tries given to the user; corresponds to the number of body parts: head, body, both arms, both legs.
    tries = 6
    #The real beginning of the game. Lets user know once the game has started with an intro, then waits for 1 second, displays the board as well as underscores for each letter that must be guessed. 
    print("")
    print(general_hint)
    time.sleep(1)
    print("\n You're all set! Let's play Hangman.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    #Code will iterate until the word is guessed or user runs out of tries.
    while not guessed and tries > 0:
        #If the user's guess is a letter, we then check if the letter is/has been a)guessed, b)not in the word, or c)in the word.
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                #Updates word_completion variable to reveal all occurences of the user's guess.
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        #Conditional for guessing a word: checks if the word has already been guessed, if it is correc/incorrect.
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        #Statement will be printed if the user input is not a letter.
        else:
            print("Not a valid guess.")
        #After each guess is handled, current state of the word will be printed.
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    #Statement 1: printed if user guessed the word correctly, statement 2: printed if user's tries are not greater than 0.
    if guessed:
        print("Congrats, you have correctly guessed the word.")
        print("You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

#Visuals; index of each stage corresponds to the number of tries which the user has left.
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

#Main function which puts everything together. 
def main():
    #Get a word from get_word().
    word = get_word()
    play(word)
    #Allowing the user to play again. Iterates until the user does not reply with 'Y' or "Yes".
    time.sleep(1)
    repeat = input("\nPlay Again? ([Y]es/[N]o) ").title()
    if repeat == "Y" or repeat == "Yes":
      word = get_word()
      play(word)
      print("Thank you for playing Hangman.")
    else: 
      print("Thank you for playing Hangman.")

if __name__ == "__main__":
    main()