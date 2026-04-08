# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
def main():
  # user input
  user_input = input("camelCase: ")
  for letter in user_input:
    # check if a letter is Capital
    check_capital = letter.isupper()
    if check_capital == True:
      letter = letter.lower()
      print("_", end="")
      print(letter, end="")
    else:
      print(letter, end="")
  print()


main()