"""
I’m thinking of a number between 1 and 100…
What is it?

It’s 50! But what if it were more random?

In a file called game.py, implement a program that:

    Prompts the user for a level, 𝑛
    . If the user does not input a positive integer, the program should prompt again.
    Randomly generates an integer between 1 and 𝑛
    , inclusive, using the random module.
    Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        If the guess is the same as that integer, the program should output Just right! and exit.

Hints

    Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html. Of particular interest, perhaps, are the functions specialized for returning integers, such as randint and randrange.

"""
import random

while True:
  try:
    user_input = int(input("Level: "))
    if user_input > 0:
      rgn = random.randint(1,user_input)
      break
  except ValueError:
    pass

while True:
  try:
    user_guess = int(input("Guess: "))
    if user_guess <= 0:
      continue
    if user_guess > rgn:
      print("Too large!")
    elif user_guess < rgn:
      print("Too small!")
    else:
      print("Just right!")
      quit()
  except ValueError:
    pass