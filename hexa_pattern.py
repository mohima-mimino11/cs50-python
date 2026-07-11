import re

def main():
  code = input("Hexadecimal color code: ").strip()
  
  pattern = r"^#[a-f0-9]{6}$"
  match = re.search(pattern, code, re.IGNORECASE)
  if match:
    print(f"Valid. Matched with {match.group()}")
  else:
    print("Invalid")
    
if __name__ == '__main__':
  main()