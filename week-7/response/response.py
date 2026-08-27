from validator_collection import checkers

email = input("What's your email address? ").strip()

valid_email = checkers.is_email(email)  # returns True

if valid_email:
  print("Valid")
else:
  print("Invalid")
