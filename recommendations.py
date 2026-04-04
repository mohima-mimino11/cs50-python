def main():
  difficulty = input("Difficult or Casual? ")
  player = input("Single Player or Multiplayer? ")
  if difficulty == "Difficult":
    if player == "Multiplayer":
      recommend("Poker")
    elif player == "Single Player":
      recommend("Klondike Solitaire")
    else:
      print("Give a valid player type")
  elif difficulty == "Casual":
    if player == "Multiplayer":
      recommend("Hearts")
    elif player == "Single Player":
      recommend("Clocks")
    else:
      print("Give a valid player type.")
  else:
    print("Please choose a valid difficulty")  
def recommend(game):
  print(f"You might like {game}!")
  
main()