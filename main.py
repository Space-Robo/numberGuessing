import random

def run():
  gettingStartNum = True
  gettingEndNum = True
  gettingNumTries = True

  print("**Number Guessing**\n")
  print("You will need to provide two numbers to create a range of numbers the computer needs to select from.")
  print("For example, if you put 1 as your start number and 100 as your end number, the computer will pick a number between 1 and 100.\n")
  
  # getting the start value of the range (making sure it's an integer)
  while gettingStartNum:
    try:
      startNum = int(input("Enter your start number: "))
      break
    except ValueError:
      print("Please enter an integer. Try again...")
  
  # getting the end value of the range (making sure it's an integer)
  while gettingEndNum:
    try:
      endNum = int(input("Enter your end number: "))
      break
    except ValueError:
      print("Please enter an integer. Try again...")

  print('The computer has selected a number bewteen ' + str(startNum) + ' and ' + str(endNum) + '!')
  print("")

  # getting the number of tries the user wants (making sure it's an integer)
  while gettingNumTries:
    try:
      numChances = int(input("How many tries would you like to guess the number?: "))
      break
    except ValueError:
      print("Please enter an integer. Try again...")
  
  # Picking a random number within the range provided
  randomNum = random.randint(startNum, endNum)

  while numChances > 0:
    gettingUserGuess = True
    print("")
    print('Chances Left: ' + str(numChances))
    # User's guess (making sure it's an integer)
    while gettingUserGuess:
      try:
        guess = int(input("Enter your guess: "))
        break
      except ValueError:
        print("Please enter an integer. Try again...")

    if guess == randomNum: # if guess matches the selected number, set numchances to -1
      numChances = -1

    elif guess > randomNum: # if guess is greater than the selected number, let the user know
      print("The number selected is less than " + str(guess) + '.')
      numChances += -1

    elif guess < randomNum: # if guess is greater than the selected number, let the user know
      print("The number selected is greater than " + str(guess) + '.')
      numChances += -1
  
  # When numChances equals -1, the computer knows the user has guessed the number
  if numChances == -1:
    print('Congratulations! You guessed the number '+ str(randomNum) + '!')
  
  # If numChances has reached 0, the game ends and the number is revealed
  else:
    print('You failed to guess the number ' + str(randomNum) + ' under the number of chances provided.')

if __name__ == "__main__":
  run()