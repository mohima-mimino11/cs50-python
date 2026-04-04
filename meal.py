# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
# Asks user for a time

# and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all.
def main():
  time = input("What time is it? ").strip()
  hour = convert(time)
  if hour >= 7 and hour <= 8:
    print("breakfast time")
  elif hour >= 12 and hour <=13:
    print("lunch time")
  elif hour >= 18 and hour <= 19:
    print("dinner time")
  else:
    return



def convert(time):
  hours, minutes = time.split(":")
  hours = float(hours)
  minutes = float(minutes) / 60
  return hours + minutes

if __name__ == "__main__":
  main()
