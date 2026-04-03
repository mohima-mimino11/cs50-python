# 
def main():
  dollars = dollars_to_float(input("How much was the meal? "))
  percent = percent_to_float(input("What percentage would you like to tip? "))
  tip = dollars * (percent/100)
  print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
  # todo
  return float(d.strip("$"))

def percent_to_float(p):
  # todo
  return float(p.strip("%"))


main()
