# name = input("What's ur name? ")

# file = open("names.txt", "w") #for writing
# file = open("names.txt", "a") #for appending
# with open("names.txt", "a") as file: ## automatically closes file
#   file.write(f"{name}\n")
# file.close()

names = []

with open("names.txt") as file: #read is default
  for line in file:
    names.append(line.rstrip())

for name in sorted(names, reverse=True): #default is False
  print(f"hello, {name}")