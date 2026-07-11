import re

locations = {"+1": "United States and Canada", "+62" : "Indonesia", "+505" : "Nicargua"}

def main():
  pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}" #naming a capture group
  number = input("Number: ").strip()
  
  match = re.search(pattern, number)
  if match:
    country_code = match.group("country_code")
    print(locations[country_code])
  else:
    print("Invalid")
  
if __name__ == "__main__":
  main()