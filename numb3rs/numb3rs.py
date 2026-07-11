import re



def main():
  print(validate(input("IPv4 Address: ")))


def validate(ip):
  if not re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
    return False
  for num in ip.split("."):
    if int(num) < 0 or int(num) > 255:
      return False
    if len(num) > 1 and num.startswith("0"):
      return False
  return True


if __name__ == "__main__":
    main()
