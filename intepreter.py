# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place

# Asks user for a mathematical expression
x, y, z = input("Expression: ").split(" ")

if y == "+":
  result = float(x) + float(z)
  print(f"{result:.1f}")
elif y == "-":
  result = float(x) - float(z)
  print(f"{result:.1f}")
elif y == "/" and z != 0:
  result = float(x) / float(z)
  print(f"{result:.1f}")
else:
  result = float(x) * float(z)
  print(f"{result:.1f}")
