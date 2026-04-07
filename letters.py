def main():
  guests = ["Mario", "Luigi", "Yoshi", "Daisy", "Bowser"]
  for guest in range(len(guests)):
    print(write_letters(guests[guest],"Princess Peach"))

def write_letters(reciever, sender):
  return f"""
  +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
  Dear {reciever},
  
  You're cordially invited to a
  a Ball at Peach's Castle this
  evening, 7:00 PM.
  
  Sincerely,
  {sender}
  +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
  """

main()