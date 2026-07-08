import re

name = input("What's ur name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name): # := Walrus operator meaning if and only if
  name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")