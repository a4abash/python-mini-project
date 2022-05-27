import random
from listOfWords import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words) # receives randomly selected valid word
    word_letters = set(word) # creates set of letters e.g slave = {'l', 'e', 'a', 's', 'v'}
    # print(word) # uncomment this line to know the output
    alphabet = set(string.ascii_uppercase) # 26 uppercase alphabet letters in set format  
    used_letters = set() #empty set

    lives = 5

    while len(word_letters) > 0 and lives > 0:
        print('You have',lives,'lives left \n')
        print('You have used these letters:', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word] # prints if letter exist else prints - in place of letter
        print('Sequence of word: ', ' '.join(word_list))

        user_letter = input("Guess a letter:").upper() # receives input from user
        if user_letter in alphabet - used_letters:  # if user_letter is valid alpahbet and is already used
            used_letters.add(user_letter) # adding to used letter set
            if user_letter in word_letters: # if guessed letter exist in set
                word_letters.remove(user_letter) # remove the letter from word_letters set
            else:
                lives = lives-1

        elif user_letter in used_letters:
            print(f'You have already used {used_letters} characeter. Please try again')

        else:
            print(f'{user_letter} is Invalid character.Please try again')

    if lives == 0:
        print("You loose the game the word was",word)
    else:
        print("You guessed the word correctly")

if __name__ == '__main__':
    hangman()
 
