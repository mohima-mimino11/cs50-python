# Asks the bank worker for greeting
greeting = input("Greeting: ").strip().lower()
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100

if(greeting.startswith('hello')):
  print("$0")
elif (greeting.startswith('h')):
  print("$20")
else:
  print("$100")
