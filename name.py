import sys

if len(sys.argv) < 2:
  sys.exit("Too Few Arguments")

for arg in sys.argv[1:-1]:
  print("My name is ", arg)