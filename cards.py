import random

def main():
  cards = ["jack", "queen", "king"]
  random.seed(0) #for debugging
  print(random.choices(cards,weights=[75, 20, 5], k=2))
  # to not get same card repeated
  # print(random.sample(cards, k=2))
main()