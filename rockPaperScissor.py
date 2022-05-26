import random

def play():
    user = str(input("Choose your weapon 'r' for rock,'p' for paper,'s' for scissors \n"))
    
    if (user !='r' and user !='p' and user !='s'): # check if entered data is valid
        print("Expected input didn't matched")
        play()
    system = random.choice(['r','p','s'])
    print(f'Sytem chose {system} and you choose {user}')

    if user == system :
        return 'It\'s a tie'
    
    if is_win(user,system)==1:
        return 'You Won'
    else:
        return 'You Loose'
        
# function to check if won, win conditon: r>s,p>r,s>p

def is_win(user,system):
    if (user == 'r' and system == 's') or (user == 'p' and system == 'r') or (user == 's' and system == 'p'):
        return 1
        
if __name__ == '__main__':
    print(play())