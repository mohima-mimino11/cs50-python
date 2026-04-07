words = {"HAIR" : 4, "PAIR" : 4, "CHAIR" : 4, "GRAPHIC" : 7}


def main():
  print("Welcome to Spelling Bee!")
  print("Your letters are: A I P C R H G")
  while len(words) > 0:
    print(f"{len(words)} words left!")
    guess = input("Guess A Word: ")
    if guess == "GRAPHIC":
      words.clear()
      print("You've Won!")
    if guess in words.keys():
      points = words.pop(guess)
      print(f"Good Job! You scored {points} points!")
  print("That's the game!")
  
main()
  