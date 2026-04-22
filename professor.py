import random


def main():
  problems = 10
  lives = 3
  score = 0
  level = get_level()
  while problems != 0:
    if lives == 3:
        x = generate_integer(level)
        y = generate_integer(level)
    try:
      answer = int(input(f"{x} + {y} = "))
      result = x + y
      if answer == result:
        score += 1
        problems -= 1
        lives = 3
        continue
      else:
        raise ValueError
    except ValueError:
      print("EEE")
      lives -= 1
      pass
    # If the user has still not answered correctly after three tries, the program should output the correct answer.
    if lives == 0:
      print(f"{x} + {y} = {result}")
      lives = 3
      problems -= 1
      continue
  print(f"Score: {score}")


def get_level():
  while True:
    try:
      user_input = input("Level: ")
      level = int(user_input)
      if level == 1 or level == 2 or level == 3:
        return level
      else:
        raise ValueError
    except ValueError:
      pass


def generate_integer(level):
  if level == 1:
    return random.randint(0, 9)
  elif level == 2:
    return random.randint(10, 99)
  elif level == 3:
    return random.randint(100, 999)




if __name__ == "__main__":
  main()
