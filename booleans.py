def main():
  difficulty = input("Difficult or Casual? ")
  if not(difficulty == "Difficult" or difficulty == "Casual"):
    print("Please choose a valid difficulty")
    return  
  player = input("Single Player or Multiplayer? ")
  if not(player == "Single Player" or player == "Multiplayer"):
    print("Give a valid player type.")
    return
  if difficulty == "Difficult" and player == "Multiplayer":
    recommend("Poker")
  elif difficulty=="Difficult" and  player == "Single Player":
    recommend("Klondike Solitaire")
  elif difficulty == "Casual" and player == "Multiplayer":
    recommend("Hearts")
  else:
    recommend("Clocks")

  
    
def recommend(game):
  print(f"You might like {game}!")
  
main()