# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
# Asks user for the great question of life, universe and everthing
answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
# If the user answers 42 or forty-two or forty two (case insensitively) print "Yes" else print "No"

if not(answer == "42" or answer == "forty-two" or answer == "forty two"):
  print("No")
else:
  print("Yes")

