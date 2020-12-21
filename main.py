import random

'''
Python Project: Number Guessing

About:
Number Guessing is a very interesting and fun game among a lot of people. 
The computer will randomly select a number from a range of numbers provided by the user.
The user will also provide how many chances they need to guess the number.
As the user is attempting to guess the number, the computer will indicate whether the number guessed is greater than, less than, or equal to the number selected by the computer.
If the user runs out of chances, it will let them know that the game is over and it will reveal the number selected.
'''

def pickNumberFromRange(start, end):
  return random.randint(start, end)

def run():
  gettingStartNum = True
  gettingEndNum = True
  gettingNumTries = True

  print("**Number Guessing**\n")
  print("You will need to provide two numbers to create a range of numbers the computer needs to select from.")
  print("For example, if you put 1 as your start number and 100 as your end number, the computer will pick a number between 1 and 100.\n")
  
  while gettingStartNum:
    try:
      startNum = int(input("Enter your start number: "))
      break
    except ValueError:
      print("Please enter an integer. Try again...")
  
  while gettingEndNum:
    try:
      endNum = int(input("Enter your end number: "))
      break
    except ValueError:
      print("Please enter an integer. Try again...")

  print('The computer has selected a number bewteen ' + str(startNum) + ' and ' + str(endNum))

  while gettingNumTries:
    try:
      numChances = int(input("How many tries would you like to guess the number?: "))
      break
    except ValueError:
      print("Please enter an integer. Try again...")
  
  randomNum = pickNumberFromRange(startNum, endNum)

  while numChances > 0:
    gettingUserGuess = True
    print("")
    print('Chances Left: ' + str(numChances))
    while gettingUserGuess:
      try:
        guess = int(input("Enter your guess: "))
        break
      except ValueError:
        print("Please enter an integer. Try again...")

    if guess == randomNum:
      numChances = -1
    elif guess > randomNum:
      print("The number selected is less than " + str(guess) + '.')
      numChances += -1
    elif guess < randomNum:
      print("The number selected is greater than " + str(guess) + '.')
      numChances += -1
  
  if numChances == -1:
    print('Congratulations! You guessed the number '+ str(randomNum) + '!')
  
  else:
    print('You failed to guess the number ' + str(randomNum) + ' under the number of chances provided.')

if __name__ == "__main__":
  run()