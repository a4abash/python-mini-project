import random
movesLeft = [1,2,3,4,5,6,7,8,9]

player1_list = []   # empty list for storing player1 move
player2_list = []   # empty list for storing computer move

def player1():
    print("*****Your turn***** \nPossible valid moves are ",movesLeft)
    user_input = int(input())
    if user_input in movesLeft: #checks if user input is valid input
        appendRemove(player1_list,movesLeft,user_input) #calling function to add user input to list and removing from available moves
        print('You choose',player1_list)
        if (len(player1_list)>2):   # calls function to check if won
            if checkIfWon(player1_list) == 1:
                print('Hurray!!! You won')
                exit()
    else:
        print('****Please enter valid moves only***')
        player1()

def appendRemove(playerlist,movesLeftlist,input):  # function to add and remove the (user and computer guess) from list
    playerlist.append(input)
    movesLeftlist.remove(input)

def player2():
    computerGuess = random.randint(1,9)
    if computerGuess in movesLeft:
        appendRemove(player2_list,movesLeft,computerGuess)
        print("Computer chose:")
        print(computerGuess,player2_list)
        if (len(player2_list)>2):       # check if won
            if checkIfWon(player2_list) == 1:
                print('Opps !!! Sorry You loose Try again')
                exit()
    else:
        player2()

def game():
    for i in range(1,10):
        player1()
        if movesLeft==[]:
            print("Out of Moves. It's a tie")
            break
        player2()

def checkIfWon(player):
    if 1 in player:
        if 2 and 3 in player: #1st row 
            return 1
        elif 4 and 7 in player: #1st column
            return 1
        elif 5 and 9 in player: #diagonal 
            return 1
    elif 2 and 5 and 8 in player: #2nd column
        return 1
    elif 3 in player:
        if 5 and 7 in player:#diagonal
            return 1
        if 6 and 9 in player: #3rd column
            return 1
    elif 4 and 5 and 6 in player: #2nd row
        return 1
    elif 7 and 8 and 9 in player: #3rd row
        return 1

if __name__ == '__main__':
    game()