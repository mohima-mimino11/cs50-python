"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:
    -“All vanity plates must start with at least two letters.”
    -“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    -“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
    AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    -“No periods, spaces, or punctuation marks are allowed.”

"""

def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):
  if len(s) < 2 or len(s) > 6:
    return False
  if not s[0].isalpha() or not s[1].isalpha():
    return False
  if not all(ch.isalnum() for ch in s):
    return False
  flag = False
  for ch in s:
    if ch.isdigit():
      flag = True
    if ch.isalpha() and flag:
      return False
  for ch in s:
    if ch.isdigit():
      return ch != "0"
  return True


if __name__ == "__main__":
  main()

