import random 
from termcolor import colored, cprint 

def welcome():
    print('''\n
😊 Welcome to guest number 😊\n
      By Abass Dev With ❤
        ''')
        
def start():
  
  rdm = random.randrange(1,10)
  guest = int(input('Enter any number between 1 & 10: '))
  tryAgain = colored('\nTRY  AGAIN ==> ', 'red')
  i = 0
     
  chance = 5
  while guest != rdm:
    i += 1
    chance -= 1
    if i >= 5:
      print(colored('\nGame Over\n', 'red'))
      newGame()
      
    elif guest > rdm:
      print('''
       ___________________
      |                   |
      | {}: High      |
      | {}: {}    |
      |___________________|'''.format(colored('STATUS', 'green'),colored('CHANCE LEFT', 'green'),chance))
      guest = int(input(tryAgain))
      
    elif guest < rdm:
      print('''
       ___________________
      |                   |
      | {}: Low       |
      | {}: {}    |
      |___________________|'''.format(colored('STATUS', 'green'),colored('CHANCE LEFT', 'green'),chance))
      guest = int(input(tryAgain))
      
    else:
      break 
    print(colored('\nBravo you win!!!','green'))
    newGame()
def newGame():
  startNewGame = input('Would you like to start again? (Y/N) ')
  if startNewGame == 'Y':
    start()
  else: 
    print('See you again!')
    quit()
  
welcome()
start()