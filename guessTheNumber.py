import random

print('Which game do you wanna play:')
print('1.Guess the random generated number by computer \n2.Let computer guess your number')
def play():
    game_num = int(input())

    if game_num == 1: # condition if user wants to play 1st game
        def guess(x):
            random_number = random.randint(1,x) #computer generates random number
            guess = 0
            while guess != random_number:
                guess = int(input(f'Guess the number between 1 and {x}\n'))
                if guess<random_number:
                    print('Too low')
                elif guess>random_number:
                    print('Too High')
            print(f"You've guessed the number correctly {random_number}\n")

        guess(50) # 0 to 50 is the range of the number that is choosed by the computer 

    elif game_num == 2: # condition if user wants to play 2nd game
        def computer_guess(x):
            low = 1
            high = x
            feedback = ''
            while feedback != 'c':
                if low==high:
                    computer_guess = low
                    break
                computer_guess = random.randint(low,high)
                print(f'System generated the number {computer_guess} ')
                feedback = (input(f'Type L if guess is low, H if guess is High or C if guess is correct ')).lower()
                if feedback == 'l':
                    low = computer_guess + 1
                elif feedback =='h':
                    high = computer_guess - 1
            print(f'System guessed your number {computer_guess} which is correct')

        computer_guess(50)

    else:
        print('Opps !!! Expected input values are 1 or 2 \nPlease enter the correct value')

if __name__ == '__main__':
    play()